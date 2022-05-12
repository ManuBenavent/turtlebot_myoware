#!/usr/bin/env python3
import rospy
from myoware_constants import *
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt32
from kobuki_msgs.msg import BumperEvent, Led, Sound
import time

# Callback datos myoware: actualiza la velocidad del turtlebot en funcion del movimiento recibido
def callback(data):
    if stop_robot:
        return
    global current_angular
    global current_linear
    data = data.data
    try:
        if data in moveBindings.keys():
            target_linear = moveBindings[data][0]*LINEAR_SPEED
            target_angular = moveBindings[data][1]*ANGULAR_SPEED
        else:
            target_linear =  0
            target_angular = 0

        if target_linear > current_linear:
            current_linear = min( target_linear, current_linear + 0.02 )
        elif target_linear < current_linear:
            current_linear = max( target_linear, current_linear - 0.02 )
        else:
            current_linear = target_linear

        if target_angular > current_angular:
            current_angular = min( target_angular, current_angular + 0.25 )
        elif target_angular < current_angular:
            current_angular = max( target_angular, current_angular - 0.25 )
        else:
            current_angular = target_angular
        
        twist = Twist()
        twist.linear.x = current_linear; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = current_angular
        print(twist)
        pub.publish(twist)
    except:
        rospy.logfatal("Se ha producido una excepcion. Robot detenido.")
    
# Callback choque: detecta bumper -> enciende leds, emite sonido, se detiene durante 2 segundos
def callback_bumper(data):
    global stop_robot
    # data.bumper: 0, 1, 2 (left, center, right)
    if data.state == 1: # Pressed
        sound = Sound()
        sound.value = Sound.CLEANINGSTART
        pub_sound.publish(sound)
        led = Led()
        led.value = Led.ORANGE
        pub_led.publish(led)
        led.value = Led.RED
        pub_led2.publish(led)
        twist = Twist()
        twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        pub.publish(twist)
        t_end = time.time() + 2
        while time.time() < t_end:
            stop_robot = True
        stop_robot = False
    else:
        led = Led()
        led.value = Led.BLACK
        pub_led.publish(led)
        pub_led2.publish(led)

if __name__=="__main__":
    rospy.init_node('turtlebot_teleop_myoware')
    # queue_size = 1 por si hay errores en sensor que se utilice lo más reciente
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)
    pub_sound = rospy.Publisher('/mobile_base/commands/sound', Sound, queue_size=1)
    pub_led = rospy.Publisher('/mobile_base/commands/led1', Led, queue_size=1)
    pub_led2 = rospy.Publisher('/mobile_base/commands/led2', Led, queue_size=1)
    rospy.Subscriber('/myoware_signal', UInt32, callback, queue_size=1)
    rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback_bumper, queue_size=1)

    current_linear = 0
    current_angular = 0
    stop_robot = False
    try:
        rospy.spin()
            
    except:
        rospy.logfatal("Se ha producido una excepcion. Robot detenido.")

    finally:
        # Por seguridad, si hay cualquier fallo ponemos velocidades a 0
        twist = Twist()
        twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        pub.publish(twist)

