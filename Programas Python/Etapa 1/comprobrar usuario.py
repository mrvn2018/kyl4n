#!/usr/bin/python

#Este script permite ingreso y lectura de nombre con sentencia while
#para la comprobacion de usuario...

print("\n")
print("##############   Autor     : Marvin Amador              ##############")
print("##############   Twitter   : @kyl4nprax                 ##############")
print("##############   Correo    : marvinamador@outlook.com   ##############")
print("\n\n")

def conwhile():
    nombre = raw_input("Ingresa tu nombre: ")
    i=0

    while (nombre != "marvin") or i<0:          #Comprueba si el usuario es incorrecto y suma la cantidad de intentos
        print('El Usuario es incorrecto\n' )
        nombre = raw_input("Ingresa tu nombre: ")
        i=i+1
        if i == 2:
            print('\n Demasiados intentos\n')   #Despues de 3 intentos sale del programa
            break

    if nombre == "marvin":
        print('\nEl Usuario es Correcto\n\n')

    print('_____FIN_____')

conwhile()
