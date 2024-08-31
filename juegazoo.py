import random
import time

puntos_persona = 0
puntos_maquina = 0
empate = 0

#Bucle que se ejecute infinito
while True:
    #Cuenta regresiva 3.2.1
    for i in range(3,0,-1):
        print(i)
        time.sleep(1) #esto es para que tarde 1 segundo en iterarse
    print('Piedra Papel o Tijera')
    #preguntando la opcion del usuario
    seleccion_yo = input('').lower()
    
    #iteracion de los ... 
    for i in range(3):
        #Imprime el punto inmediatamente el bucle pase, (end ='') esto es para que se ejecute en la misma linea 
        print('.',end='',flush=True) 
        time.sleep(1)
    print()
    manos = ['Piedra', 'Papel', 'Tijera']
    #Escoje un elemento aleatorio de la lista
    aleatorio_manos = random.choice(manos) 
    print(aleatorio_manos)

    if aleatorio_manos.lower() == seleccion_yo.lower():
        empate += 1
        print(f'Ha sido empate!!!, veces empate: {empate}')
        
    elif aleatorio_manos.lower() == 'piedra' and seleccion_yo.lower() == 'tijera' or aleatorio_manos.lower() == 'tijera' and seleccion_yo.lower() == 'papel' or aleatorio_manos.lower() == 'papel' and seleccion_yo.lower() == 'piedra':
        puntos_maquina +=1
        print(f'Has perdido :), veces perdido {puntos_maquina}')
    elif aleatorio_manos.lower() == 'tijera' and seleccion_yo.lower() == 'piedra' or aleatorio_manos.lower() == 'papel' and seleccion_yo.lower() == 'tijera' or aleatorio_manos.lower() == 'piedra' and seleccion_yo.lower() == 'papel':
        puntos_persona +=1
        print(f'Has ganado!! ):, veces ganada: {puntos_persona}')
    else:
        print('Ha ocurrido un error, al parecer ingresaste algo incorrecto')
        

