# Movements
STOP = 0
MOVE_FORWARD = 1
MOVE_BACKWARD = 2
TURN_LEFT = 3
TURN_RIGHT = 4

moveBindings={
    STOP:(0,0),
    MOVE_FORWARD:(1,0),
    MOVE_BACKWARD:(-1,0),
    TURN_LEFT:(0,1),
    TURN_RIGHT:(0,-1)
}
moveString={
    STOP:"stop",
    MOVE_FORWARD:"delante",
    MOVE_BACKWARD:"atras",
    TURN_LEFT:"izquierda",
    TURN_RIGHT:"derecha"
}

# Speed
LINEAR_SPEED = .2
ANGULAR_SPEED = 1

umbral1=3000
umbral2=3750

PUERTO_SERIE = '/dev/ttyUSB1'