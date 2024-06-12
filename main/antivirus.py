import pandas as pd
import random
import time

# Variable global para almacenar la información del usuario
usuario = {
    "nombre": "",
    "puntuacion": 0
}

def cargar_preguntas(archivo_excel):
    # Leer el archivo de Excel
    df = pd.read_excel('C:/python/ppi/main/preguntas.xlsx')
    return df

def seleccionar_preguntas(df, modulo, nivel, num_preguntas=5):
    # Filtrar las preguntas según el módulo y nivel
    preguntas_filtradas = df[(df['Módulo'] == modulo) & (df['Nivel'] == nivel)]
    # Seleccionar preguntas aleatorias
    preguntas_seleccionadas = preguntas_filtradas.sample(n=num_preguntas)
    return preguntas_seleccionadas

def jugar():
    global usuario
    
    # Cargar el banco de preguntas
    banco_preguntas = cargar_preguntas('preguntas.xlsx')

    # Pedir al usuario que elija un módulo y nivel de dificultad
    modulo = input("Elige un módulo (Matemáticas, Álgebra, Geometría): ")
    nivel = input("Elige un nivel (Fácil, Intermedio, Difícil): ")

    # Seleccionar preguntas
    preguntas = seleccionar_preguntas(banco_preguntas, modulo, nivel)

    # Definir el límite de tiempo según el nivel
    if nivel.lower() == "fácil":
        tiempo_limite = 15
    elif nivel.lower() == "intermedio":
        tiempo_limite = 20
    elif nivel.lower() == "difícil":
        tiempo_limite = 30
    else:
        print("Nivel no válido. Se establecerá el tiempo límite a 30 segundos.")
        tiempo_limite = 30

    vidas = 3
    puntuacion = 0

    # Mostrar las preguntas al usuario
    for index, pregunta in preguntas.iterrows():
        print("\nPregunta:", pregunta['Pregunta'])
        print("A.", pregunta['Opción A'])
        print("B.", pregunta['Opción B'])
        print("C.", pregunta['Opción C'])
        print("D.", pregunta['Opción D'])

        start_time = time.time()
        respuesta_usuario = input(f"Tu respuesta (A-D): ").upper()
        tiempo_transcurrido = time.time() - start_time

        if tiempo_transcurrido > tiempo_limite:
            print(f"Tiempo agotado. Tenías {tiempo_limite} segundos para responder.")
            vidas -= 1
        elif respuesta_usuario == pregunta['Respuesta Correcta']:
            print("¡Correcto!")
            puntuacion += 1
        else:
            print("Incorrecto. La respuesta correcta era:", pregunta['Respuesta Correcta'])
            vidas -= 1

        print(f"Te quedan {vidas} vidas.")
        if vidas == 0:
            print("Has perdido todas tus vidas. Juego terminado.")
            break

    if vidas > 0:
        print("¡Felicidades! Has completado todas las preguntas.")

    usuario['puntuacion'] = puntuacion
    print(f"Tu puntuación final es: {puntuacion}")

def perfil_usuario():
    global usuario
    if usuario["nombre"]:
        print(f"Nombre de usuario: {usuario['nombre']}")
        print(f"Puntuación: {usuario['puntuacion']}")
    else:
        print("No hay usuario registrado.")

def registrar_usuario():
    global usuario
    usuario["nombre"] = input("Escribe tu nombre de usuario: ")
    usuario["puntuacion"] = 0
    print(f"Usuario {usuario['nombre']} registrado con éxito.")

def ingresar_usuario():
    global usuario
    nombre = input("Escribe tu nombre de usuario: ")
    usuario["nombre"] = nombre
    # La puntuación se podría cargar de algún sistema de almacenamiento si se necesita persistencia
    usuario["puntuacion"] = 0
    print(f"Usuario {usuario['nombre']} ingresado con éxito.")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar")
        print("2. Perfil de usuario")
        print("3. Salir")
        opcion = input("Elige una opción (1-3): ")

        if opcion == '1':
            jugar()
        elif opcion == '2':
            perfil_usuario()
        elif opcion == '3':
            print("Saliendo del juego...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 3.")

if __name__ == "__main__":
    while True:
        print("1. Registrarse")
        print("2. Ingresar")
        opcion = input("Elige una opción (1-2): ")
        if opcion == '1':
            registrar_usuario()
            menu_principal()
        elif opcion == '2':
            ingresar_usuario()
            menu_principal()
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 2.")

