#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import UInt32
from myoware_constants import *
import select, sys


def callback(data):
    data = data.data
    twist = Twist()
    try:
        if data == STOP:
            twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        elif data == MOVE_FORWARD:
            twist.linear.x = 0.2; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
        elif data == TURN_LEFT:
            twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 1
        elif data == TURN_RIGHT:
            twist.linear.x = 0; twist.linear.y = 0; twist.linear.z = 0
            twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = -1
        pub.publish(twist)
    except:
        rospy.logfatal("Se ha producido una excepcion. Robot detenido.")
    

if __name__=="__main__":
    rospy.init_node('turtlebot_teleop_myoware')
    pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=5)
    rospy.Subscriber('/myoware_signal', UInt32, callback, queue_size=5)

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

