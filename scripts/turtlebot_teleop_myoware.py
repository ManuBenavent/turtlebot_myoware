#!/usr/bin/env python

import rospy
import select, sys
from myoware_constants import *
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt32
from kobuki_msgs.msg import BumperEvent

# Callback datos myoware: actualiza la velocidad del turtlebot en funcion del movimiento recibido
def callback(data):
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

        # TODO: continuar movimiento si se recibe 0 hasta que se reciba más veces?
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
        pub.publish(twist)
    except:
        rospy.logfatal("Se ha producido una excepcion. Robot detenido.")
    

def callback_bumper(data):
    # data.bumper: 0, 1, 2 (left, center, right)
    if data.state == 1: # Pressed
        twist = Twist()
        twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        pub.publish(twist)
        # TODO: decidir entre PARAR/MARCHA ATRAS/LED/SONIDO

if __name__=="__main__":
    rospy.init_node('turtlebot_teleop_myoware')
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=5)
    rospy.Subscriber('/myoware_signal', UInt32, callback, queue_size=5)
    rospy.Subscriber('/mobile_base/events/bumper', BumperEvent, callback_bumper, queue_size=5)

    current_linear = 0
    current_angular = 0
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

