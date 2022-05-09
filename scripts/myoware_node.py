#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt32
from myoware_constants import *
import serial, time
import re

import select, sys
umbral1=4000
umbral2=4000

arduino = serial.Serial('COM4', 9600)
time.sleep(2)
rawString = arduino.readline()
flexion = 0
extension = 0
cont=0
valor_anterior_f=0
valor_anterior_e=0

if __name__ == "__main__":
    rospy.init_node('myoware_node')
    pub = rospy.Publisher('/myoware_signal', UInt32, queue_size=5)

    while True:
        # rlist, _, _ = select.select([sys.stdin], [], [], 5)
        # if rlist:
        #     try:
        #         key = int(sys.stdin.read(1))
        #         if key not in range(4):
        #             key = STOP
        #     except:
        #         key = STOP
        # else:
        #     key = STOP
        # pub.publish(key)

        rawString = arduino.readline()
        valor = rawString.decode("utf-8")
        
        
        valores=valor.split()
        # print("0: ",valores[0])
        # print("1: ",valores[1])

        
        # if(valor[0] == 0):
            #for i in range(2, len(valor)):

            # flexion = flexion[1:]
            
        # elif(valor[0] == 1):
            # extension = valor[1:]

        #time.sleep(0.05)
        # print("valor: ", valor)

        if int(valores[0])>umbral1 and int(valores[1])<umbral2:
                command=TURN_LEFT
        elif int(valores[0])<umbral1 and int(valores[1])>umbral2:
                command=TURN_RIGHT
        elif int(valores[0])>umbral1 and int(valores[1])>umbral2:
                command=MOVE_FORWARD
        else:
                command=STOP
                
        print ("estado: ", command)
        pub.publish(command)
    