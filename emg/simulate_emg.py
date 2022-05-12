with open('signal2.txt','w') as f:
    # Delante
    for i in range(118):
        f.write("4000 0\n")
    # Cambio a giro
    for i in range(20):
        f.write("4000 4000\n")

    # Giro izquierda
    for i in range(18):
        f.write("4000 0\n")
    # Cambio a avanzar
    for i in range(20):
        f.write("4000 4000\n")

    # Atras
    for i in range(40):
        f.write("0 4000\n")

    # Cambio a giro
    for i in range(20):
        f.write("4000 4000\n")
    
    # Giro derecha
    for i in range(23):
        f.write("0 4000\n")
    # Stop
    for i in range(18):
        f.write("0 0\n")
    # Giro derecha
    for i in range(21):
        f.write("0 4000\n")
    # Cambio a avanzar
    for i in range(20):
        f.write("4000 4000\n")
    # Delante
    for i in range(42):
        f.write("4000 0\n")
    # Cambio a giro
    for i in range(20):
        f.write("4000 4000\n")
    # Giro izquierda
    for i in range(18):
        f.write("4000 0\n")
    # Cambio a avanzar
    for i in range(20):
        f.write("4000 4000\n")
    # Delante
    for i in range(57):
        f.write("4000 0\n")
    # Cambio a giro
    for i in range(20):
        f.write("4000 4000\n")
    # Giro izquierda
    for i in range(18):
        f.write("4000 0\n")
    # Cambio a avanzar
    for i in range(20):
        f.write("4000 4000\n")
    # Delante
    for i in range(80):
        f.write("4000 0\n")
    # Cambio a giro
    for i in range(20):
        f.write("4000 4000\n")
    # Giro izquierda
    for i in range(21):
        f.write("4000 0\n")
    # Cambio a avanzar
    for i in range(20):
        f.write("4000 4000\n")
    # Delante
    for i in range(180):
        f.write("4000 0\n")
    

    
    # f.write("4000 4000\n")

    # for i in range(40):
    #     f.write("4000 0\n")
    # f.write("4000 4000\n")

    # f.write("4000 4000\n")
    # for i in range(10):
    #     f.write("4000 0\n")