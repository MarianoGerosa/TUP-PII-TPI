import libro as l


# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)


def ejemplares_prestados():

    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    codigo_ingresado=input("Ingrese el código del libro")
    for libro in libros:
        if libro['cod'] == codigo_ingresado:

            print(f"Autor:{libro['autor']}\nNombre:{libro['titulo']}\nDisponibles:{libro['cant_ej_ad']}")

            if libro['cant_ej_ad'] > 0:
                retirar=input("Desea retirar un libro? S - N")
                
                # VALIDAR LA RESPUESTA S - N
        
                if retirar.upper() == "S":
                    libro['cant_ej_ad']-=1
                    print(f"Disponibles:{libro['cant_ej_ad']}")
                    print("Libro prestado con exito")
                    return None
                else:
                    print("Libro no prestado")
                    return None
            else:
                print("No hay ejemplares para prestar")
                return None
        elif libro['cod']!= codigo_ingresado and libro == libros[-1]:
            print("Libro no encontrado")
            
    return None

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None