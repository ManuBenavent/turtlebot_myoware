#!/usr/bin/env python3

import rospy
from std_msgs.msg import UInt32
from myoware_constants import *

estado = 1 # empieza avanzando

if __name__ == "__main__":
    rospy.init_node('myoware_node')
    pub = rospy.Publisher('/myoware_signal', UInt32, queue_size=1)

    with open('/home/manu/catkin_ws/src/turtlebot_myoware/emg/signal.txt') as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    for valor in lines:
        try:
                print(valor)
                valores=valor.split()

                if estado == 0:
                        if int(valores[0])>umbral1 and int(valores[1])<umbral2:
                                command=TURN_LEFT
                        elif int(valores[0])<umbral1 and int(valores[1])>umbral2:
                                command=TURN_RIGHT
                        elif int(valores[0])>umbral1 and int(valores[1])>umbral2:
                                estado = 1
                                command = STOP
                                rospy.sleep(rospy.Duration(secs=1))
                        else:
                                command=STOP

                elif estado == 1:
                        if int(valores[0])>umbral1 and int(valores[1])<umbral2:
                                command=MOVE_FORWARD
                        elif int(valores[0])<umbral1 and int(valores[1])>umbral2:
                                command=MOVE_BACKWARD
                        elif int(valores[0])>umbral1 and int(valores[1])>umbral2:
                                estado = 0
                                command = STOP
                                rospy.sleep(rospy.Duration(secs=1))
                        else:
                                command=STOP
                
                estado_str = 'avanzar' if estado==1 else 'giro'

                print (f"Estado: {estado_str}")
                print (f"Command: {moveString[command]}")
                pub.publish(command)
                # 
                rospy.sleep(rospy.Duration(secs=0.1))
        except:
                rospy.logerr("Excepcion")
    