# Trabajo Práctico I - Programación II

import bibloteca as biblio
import os


#probando git

print("Bienvenido!")
respuesta = ''

def menu():
    os.system ("cls")
    print("1 - Gestionar Prestamo")
    print("2 - Gestionar Devolución")
    print("3 - Registrar nuevo libro")
    print("4 - Eliminar ejemplar")
    print("5 - Mostrar ejemplares prestados")
    print("6 - Salir")

while respuesta != "salir":
    menu()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            biblio.prestar_ejemplar_libro()
        elif int(opt) == 2:
            biblio.devolver_ejemplar_libro()
            print()
        elif int(opt) == 3:
            biblio.nuevo_libro()
            print()
        elif int(opt) == 4:
            biblio.eliminar_ejemplar_libro()
            print()
        elif int(opt) == 5:
            biblio.ejemplares_prestados()
            print()
        elif int(opt) == 6:
            respuesta = "salir"
        else: print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")