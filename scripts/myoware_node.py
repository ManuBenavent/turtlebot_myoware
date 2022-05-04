#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt32
from myoware_constants import *

import select, sys

if __name__ == "__main__":
    rospy.init_node('myoware_node')
    pub = rospy.Publisher('/myoware_signal', UInt32, queue_size=5)

    while True:
        rlist, _, _ = select.select([sys.stdin], [], [], 5)
        if rlist:
            try:
                key = int(sys.stdin.read(1))
                if key not in range(4):
                    key = STOP
            except:
                key = STOP
        else:
            key = STOP
        pub.publish(key)
    
    