import random

LINEAS_MAXIMAS = 3
SLOTS = ["♦", "♣", "♥"]
MONTO_MINIMO = 5

def deposito ():
    while True:
        try:
            dep = int(input("Ingrese un monto a depositar (Monto mínimo 5$): "))
            if dep < MONTO_MINIMO:
                raise ValueError
            else:
                return dep
        except ValueError:
            print ("Error: Ingrese un monto válido")
            
def lineas_a_jugar ():
    while True:
        try:
            lineas = int(input(f"¿Cuantas líneas quiere jugar? (Maximo: {LINEAS_MAXIMAS}): "))
            if (lineas < 1 or lineas > LINEAS_MAXIMAS):
                raise ValueError
            else:
                return lineas
        except ValueError:
            print ("Error: Ingrese una cantidad valida")
    
def jugar (lineas, slot1, slot2, slot3, monto):
    ganancia = 0
    while True:
        try:
            apostar = int(input("¿Cuanto vas a apostar? (Monto mínimo 5$): "))
            if apostar < MONTO_MINIMO:
                raise ValueError
            elif apostar > monto:
                raise ValueError
            else:
                monto = monto - apostar
                break
        except ValueError:
            print ("Error: Monto no válido o mayor al saldo disponible")
    
    for i in range (len(SLOTS)):
        print ("|" + slot1[i] + "|" + slot2[i] + "|" + slot3[i] + "|", end="" )
        print ()
            
    if (slot1[1] == slot2[1] and slot1[1] == slot3[1]):
        print("¡Ganaste en la línea 1!")
        ganancia = ganancia + apostar * 3
     
    if (lineas >= 2):   
        if (slot1[0] == slot2[0] and slot1[0] == slot3[0]):
            print("¡Ganaste en la línea 2!")
            ganancia = ganancia + apostar * 2
        
        if (slot1[2] == slot2[2] and slot1[2] == slot3[2]):
            print("¡Ganaste en la línea 2!")
            ganancia = ganancia + apostar * 2             
    
    if (lineas == 3):
        if (slot1[0] == slot2[1] and slot1[0] == slot3[2]):
            print("¡Ganaste en la línea 3!")
            ganancia = ganancia + apostar * 1.5
            
        if (slot1[2] == slot2[1] and slot1[2] == slot3[0]):
            print("¡Ganaste en la línea 3!")
            ganancia = ganancia + apostar * 1.5
        
    print (f"Ganaste: {ganancia}$")
    nuevo_monto = monto + ganancia
    print (f"Tienes {nuevo_monto}$ de saldo")
    return nuevo_monto
    

def mezclar ():
    numero_aleatorio = random.randint(0, (len(SLOTS) - 1))
    cont = 0
    slot_aleatorio = []
    numeros_aleatorios = []
    
    for i in range (len(SLOTS)):
        numeros_aleatorios.append(i)
    
    random.shuffle(numeros_aleatorios)
    
    for i in range (len(SLOTS)):
        slot_aleatorio.append(SLOTS[numeros_aleatorios[i]])

    return slot_aleatorio

def main():            
    monto = deposito()
    repeat = "a"
    while repeat != "0":
        if monto < MONTO_MINIMO:
            print ("Fondos insuficientes")
            monto = deposito()
            monto = monto + nuevo_monto
        
        print("\n")
        
        lineas = lineas_a_jugar()
        
        slot1 = mezclar()
        slot2 = mezclar()
        slot3 = mezclar()
        
        print("\n")
        
        nuevo_monto = jugar(lineas, slot1, slot2, slot3, monto)
        monto = nuevo_monto
        
        repeat = input ("""                        
¿Quieres seguir jugando?                        
Presiona cualquier tecla para seguir jugando, o presiona '0' para salir: """)


main ()
            