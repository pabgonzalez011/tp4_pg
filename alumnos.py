# alumnos.py - Componente principal del sistema

def agregar_alumno(alumnos, nombre):
    alumnos.append(nombre)

def eliminar_alumno(alumnos, nombre):
    if nombre in alumnos:
        alumnos.remove(nombre)

if __name__ == "__main__":
    print("Sistema de Alumnos TP4 v0.1")
    alumnos = ["Juan", "Maria", "Pedro"]
    print("Alumnos registrados:")
    for alumno in alumnos:
        print("-", alumno)