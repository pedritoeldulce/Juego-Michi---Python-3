## Michi Version 1
## By Paolo Perez Ttito

import random 


#variables para PC y Oponente 
pc=10
oponente=1

#tablero=[0,1,1,0,10,0,0,10,1]
#crea tablero nuevo
def crear_tablero():
    tablero=[0,0,0,0,0,0,0,0,0]
    #print(tablero)
    return tablero



#Convierte valores de 1 -> O e 10 -> X
def convertir_a_letras(v):
    if (v == 1):
        return 'O'
    elif (v == 10):
        return 'X'
    elif (v == 0):
        return " "
    
def imprimir_fila(x ,y ,z):
     print("    {0}  |  {1}  |  {2} ".format(convertir_a_letras(x),convertir_a_letras(y),convertir_a_letras(z)))
     

def imprimir_tablero(tablero):
    print("\n")
    imprimir_fila(tablero[0],tablero[1],tablero[2])
    print('   ----------------')
    imprimir_fila(tablero[3],tablero[4],tablero[5])
    print('   ----------------')
    imprimir_fila(tablero[6],tablero[7],tablero[8])
    print("\n")
    

    
def efectuar_movimiento(jugador,pos, tablero):
    pos=pos
    tablero[pos-1]=jugador
    return tablero

    
#Suma y devulve las tripletas    
def suma_tripleta(tablero):
    sumas=[]
    tripleta1,tripleta2,tripleta3=0,0,0
    tripleta4,tripleta5,tripleta6=0,0,0
    tripleta7,tripleta8=0,0
    
    for i in tablero[0:3]:
        tripleta1=tripleta1+i
        
        
    for i in tablero[3:6]:
        tripleta2=tripleta2+i
              
    for i in tablero[6:9]:
        tripleta3=tripleta3+i
       
    for i in range(0,7,3):
        tripleta4=tripleta4+tablero[i]

    for i in range(1,8,3):
        tripleta5=tripleta5+tablero[i]
        
    for i in range(2,9,3):
        tripleta6=tripleta6+tablero[i]
    
    for i in range(0,9,4):
        tripleta7=tripleta7+tablero[i]
        
    for i in range(2,7,2):
        tripleta8=tripleta8+tablero[i]
        
        
    sumas=[tripleta1,tripleta2,tripleta3,tripleta4,tripleta5,tripleta6,tripleta7,tripleta8]
    return sumas
    #print(sumas)
    

def ganador_p(tablero):
    sumas= suma_tripleta(tablero) #se guarda la suma de tripletas en la lista sumas
    gana_op=False
    gana_pc=False
    
        
    for i in range(len(sumas)):
        if oponente*3==sumas[i]:
            gana_op=True
            #print(ganador)
            
    for i in range(len(sumas)):
        if pc*3==sumas[i]:
            gana_pc=True
            #print(ganador)        
            
    if gana_op==True and gana_pc==False:
        ganador=gana_op
    elif gana_op==False and gana_pc==True:
        ganador=gana_pc
    else:
        ganador=False
    return ganador 

def inicio():
    
    print("""\n
          
          ------ JUEGO DEL MICHI -----
          NOTA:
              
              OPONENTE: O
              PC      : X
              
          Le gustaria comenzar el juego?
          [1] Si
          [2] NO
          [3] Salir
    """)
    opcion=int(input("Seleccione la opcion: \n"))
    
    if opcion == 1:
        #print('oponente incia juego')
        movimiento_oponente(crear_tablero())
    elif opcion ==2:
        #print ('maquina inicia juego')
        movimiento_pc(crear_tablero())
    elif opcion==3:
        print("\n")
        print("Saliendo ...")


def validar_movimiento(tablero):
    global cent
    #print(tablero)
    pos=int(input("Ingrese tu movimiento: ")) 
    print("\n")
    if(tablero[pos-1]==0 ):
        pos=pos
        cent = pos
    else:
        #pos=int(input("Ingrese un movimiento valido: ")) 
        print("casilla ocupada")
        validar_movimiento(tablero)
     
    return pos
   

def movimiento_oponente(tablero):
    
    posi=(validar_movimiento(tablero))
    
    nuevo_tablero=(efectuar_movimiento(oponente,cent,tablero))
    
    print("Mi movimiento: ",posi)
    imprimir_tablero(nuevo_tablero)
    
    if ganador_p(nuevo_tablero) == True:
        print("    Gana Oponente")
        inicio()
    elif tablero_total_p == True:
        print("    Empate")
    else:
        movimiento_pc(nuevo_tablero)
    

def tablero_total_p(tablero): #Retorna True si no hay celdas vacias
    
    for i in tablero:
        #print(len(tablero))
        #print(tablero[i])
        if tablero[i] == 0:
            print(tablero[i])
            return False
        else:
            return True



def movimiento_pc(tablero):
    print("ahora  toca jugar a la PC")
    print("\n")
    mejor_movimiento = escoger_estrategia_pc(tablero)
    pos = mejor_movimiento[0]
    estrategia = mejor_movimiento[1]
    
    nuevo_tablero = (efectuar_movimiento(pc, pos, tablero))
    
    print("movimientos: " ,pos )
    print("Estrategia: ", estrategia)
    
    imprimir_tablero(nuevo_tablero)
    
    if ganador_p(nuevo_tablero) == True:
        print("    Gana PC")
        inicio()
    elif tablero_total_p == True:
        print("    Empate")
    else:
        movimiento_oponente(nuevo_tablero)
    
    #return tablero
    
    
def escoger_estrategia_pc(tablero):
    return estrategia_aleatoria(tablero)
    
    
def estrategia_aleatoria(tablero):
   
    valor=seleccion_aleatoria_casillero_vacio(tablero).pop()
    
    
    tupla= valor,"Movimiento Aleatorio"
    
    return tupla


cola =[]

def seleccion_aleatoria_casillero_vacio(tablero):
    global cola
    pos=random.randint(0,8)
    
    if (tablero[pos-1]!= 0):
        while (tablero[pos-1]!= 0):
            pos=random.randint(0,8)
    
    cola.append(pos)
     
    if (tablero[pos-1]==0):
        return cola
        
    else:
        seleccion_aleatoria_casillero_vacio(tablero)
        return cola
    
    return cola.pop()


inicio()





