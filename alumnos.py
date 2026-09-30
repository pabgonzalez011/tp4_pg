# alumnos.py - Componente principal del sistema mejorado

def agregar_alumno(alumnos, nombre):
    alumnos.append(nombre)
    print(f"Alumno {nombre} agregado con éxito.")

def eliminar_alumno(alumnos, nombre):
    if nombre in alumnos:
        alumnos.remove(nombre)
        print(f"Alumno {nombre} eliminado.")
    else:
        print("El alumno no se encuentra en la lista.")

def buscar_alumno(alumnos, nombre):
    if nombre in alumnos:
        print(f"El alumno {nombre} está registrado.")
        return True
    print(f"El alumno {nombre} NO está registrado.")
    return False

if __name__ == "__main__":
    print("Sistema de Alumnos TP4 v0.2 con funciones avanzadas")

    lista_alumnos = ["Juan", "Maria", "Pedro", "Lucia"]

    print("Alumnos registrados inicialmente:")
    for alumno in lista_alumnos:
        print("-", alumno)

    # Pruebas de funciones nuevas
    buscar_alumno(lista_alumnos, "Maria")
    agregar_alumno(lista_alumnos, "Carlos")