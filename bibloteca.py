import libro as l
import cod_generator as cg


# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def ejemplares_prestados():
    for libro in libros:
        if libro['cant_ej_pr'] > 0:
            print(f"Nombre: {libro['titulo']}\nPrestados: {libro['cant_ej_pr']}\n")
        else:
            print(f"No hay ejemplares prestados del libro {libro['titulo']}\n")
    return None



def eliminar_ejemplar_libro():
    codigo_ingresado=input("Ingrese el código del libro: ")
    for libro in libros:
        if libro['cod'] == codigo_ingresado: 
            if libro['cant_ej_ad'] > 0:
                print(f"Autor:{libro['autor']}\nNombre:{libro['titulo']}\nDisponibles:{libro['cant_ej_ad']}")
                eli=int(input("Ingrese cuantos ejemplares quiere eliminar: "))
                if eli > libro['cant_ej_ad']:
                    print("No se puede eliminar mas ejemplares de los que hay, intente nuevamente")
                    return None
                else:
                    libro['cant_ej_ad'] -= eli
                    print("Se eliminó el ejemplar del libro correctamente")
                    return None
            else:
                print("No hay ejemplares disponibles")
                return None
    print("No se encontro el libro en la lista")
    return None

def prestar_ejemplar_libro():
    codigo_ingresado=input("Ingrese el código del libro: ")
    for libro in libros:
        if libro['cod'] == codigo_ingresado:
            print(f"Autor:{libro['autor']}\nNombre:{libro['titulo']}\nDisponibles:{libro['cant_ej_ad']}")
            if libro['cant_ej_ad'] > 0:
                while True:
                    retirar=input("Desea retirar un libro? S - N \n")
                    if retirar.upper() == "S":
                        libro['cant_ej_ad']-=1
                        libro['cant_ej_pr']+= 1
                        print(f"Disponibles:{libro['cant_ej_ad']}")
                        print("Libro prestado con exito")
                        return None
                    elif retirar.upper() == "N":
                        print("Libro no prestado")
                        return None
                    else:
                        print("Ingrese (s o S) para retirar el libro o (n o N) para no hacerlo \n")
            else:
                print("No hay ejemplares para prestar")
                return None
        elif libro['cod']!= codigo_ingresado and libro == libros[-1]:
            print("Libro no encontrado")
    return None

def devolver_ejemplar_libro():
    codigo_ingresado=input("Ingrese el código del libro")
    for libro in libros:
        if libro['cod'] == codigo_ingresado: 
            if libro['cant_ej_pr'] > 0:
                print(f"Hay {libro['cant_ej_pr']} prestados")
                while True:
                        devolver=input("Desea devolver un libro? S - N \n").upper()
                        if devolver == "S":
                            libro['cant_ej_pr'] -= 1
                            libro['cant_ej_ad'] += 1
                            print("Libro devuelto con exito")
                            return None
                        elif devolver == "N":
                            print("No se devolvio el libro")
                            return None
                        else:
                            print("Ingrese (s o S) para devolver el libro o (n o N) para no hacerlo \n")
                else:
                    print("No hay libros prestados")
                    return None

    print("No se encontro el libro en la lista")

    return None

def nuevo_libro():
    contador=0
    for libro in libros:
        contador+=1
    contador+=1
    conta_str = str(contador)
    libros.append("libro"+conta_str)

    codigo=cg.generar()
    nombre_ejemplar=input("Ingrese el nombre del libro: ")
    autor_ingresar=input("Ingrese el nombre del Autor: ")
    cant_ej_adquiridos=int(input("Ingrese la cantidad de ejemplares que desea ingresar al sistema: "))

    libros[-1]={'cod': codigo, 'cant_ej_ad': cant_ej_adquiridos, 'cant_ej_pr': 0, "titulo": nombre_ejemplar, "autor": autor_ingresar}
    dicc=libros[-1]
    print(f"RESUMEN\nAutor:{dicc['autor']}\nNombre:{dicc['titulo']}\nDisponibles:{dicc['cant_ej_ad']}")
    
    return None