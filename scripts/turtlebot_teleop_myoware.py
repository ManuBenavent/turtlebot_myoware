#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt32
from myoware_constants import *
import select, sys

linear_speed = .5
angular_speed = 1

moveBindings={
    STOP:(0,0),
    MOVE_FORWARD:(1,0),
    TURN_LEFT:(0,1),
    TURN_RIGHT:(0,-1)
}

def callback(data):
    global current_angular
    global current_linear
    data = data.data
    try:
        if data in moveBindings.keys():
            target_linear = moveBindings[data][0]*linear_speed
            target_angular = moveBindings[data][1]*angular_speed
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
        # if data == STOP:
        #     twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        #     twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        # elif data == MOVE_FORWARD:
        #     twist.linear.x = 0.2; twist.linear.y = 0; twist.linear.z = 0
        #     twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        # elif data == TURN_LEFT:
        #     twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        #     twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 1
        # elif data == TURN_RIGHT:
        #     twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
        #     twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -1
        twist = Twist()
        twist.linear.x = current_linear; twist.linear.y = 0; twist.linear.z = 0
        twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = current_angular
        pub.publish(twist)
    except:
        rospy.logfatal("Se ha producido una excepcion. Robot detenido.")
    

if __name__=="__main__":
    rospy.init_node('turtlebot_teleop_myoware')
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=5)
    rospy.Subscriber('/myoware_signal', UInt32, callback, queue_size=5)

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

