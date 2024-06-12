import pandas as pd
import random
import time
import tkinter as tk
from tkinter import messagebox

# Variable global para almacenar la información del usuario
usuario = {
    "nombre": "",
    "puntuacion": 0
}

# Ruta completa al archivo de preguntas
ruta_archivo = 'C:\python\ppi\main\preguntas.xlsx'

def cargar_preguntas(archivo_excel):
    # Leer el archivo de Excel
    df = pd.read_excel(archivo_excel)
    print("Columnas del DataFrame:", df.columns)
    return df

def seleccionar_preguntas(df, modulo, nivel, num_preguntas=5):
    preguntas_filtradas = df[(df['Módulo'] == modulo) & (df['Nivel'] == nivel)]
    preguntas_seleccionadas = preguntas_filtradas.sample(n=num_preguntas)
    return preguntas_seleccionadas

class Juego:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Preguntas")
        self.root.geometry("600x400")
        
        self.crear_pantalla_inicio()

    def crear_pantalla_inicio(self):
        self.limpiar_pantalla()
        
        tk.Label(self.root, text="Bienvenido al Juego de Preguntas", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Button(self.root, text="Registrarse", command=self.registrar_usuario).pack(pady=10)
        tk.Button(self.root, text="Ingresar", command=self.ingresar_usuario).pack(pady=10)

    def registrar_usuario(self):
        self.limpiar_pantalla()
        
        tk.Label(self.root, text="Registrarse", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Nombre de usuario:").pack()
        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.pack(pady=5)
        
        tk.Button(self.root, text="Registrar", command=self.guardar_usuario).pack(pady=10)

    def ingresar_usuario(self):
        self.limpiar_pantalla()
        
        tk.Label(self.root, text="Ingresar", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Nombre de usuario:").pack()
        self.entry_usuario = tk.Entry(self.root)
        self.entry_usuario.pack(pady=5)
        
        tk.Button(self.root, text="Ingresar", command=self.guardar_usuario).pack(pady=10)

    def guardar_usuario(self):
        global usuario
        nombre = self.entry_usuario.get()
        if nombre:
            usuario["nombre"] = nombre
            usuario["puntuacion"] = 0
            messagebox.showinfo("Éxito", f"Usuario {nombre} registrado/ingresado con éxito")
            self.crear_menu_principal()
        else:
            messagebox.showwarning("Error", "El nombre de usuario no puede estar vacío")

    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        tk.Label(self.root, text=f"Bienvenido, {usuario['nombre']}", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Button(self.root, text="Jugar", command=self.jugar).pack(pady=10)
        tk.Button(self.root, text="Perfil de usuario", command=self.perfil_usuario).pack(pady=10)
        tk.Button(self.root, text="Salir", command=self.crear_pantalla_inicio).pack(pady=10)

    def perfil_usuario(self):
        self.limpiar_pantalla()
        
        tk.Label(self.root, text="Perfil de Usuario", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.root, text=f"Nombre de usuario: {usuario['nombre']}").pack()
        tk.Label(self.root, text=f"Puntuación: {usuario['puntuacion']}").pack(pady=5)
        
        tk.Button(self.root, text="Volver al Menú Principal", command=self.crear_menu_principal).pack(pady=10)

    def jugar(self):
        self.limpiar_pantalla()
        
        tk.Label(self.root, text="Elige un módulo", font=("Helvetica", 16)).pack(pady=20)
        
        self.modulo = tk.StringVar()
        self.nivel = tk.StringVar()
        
        modulos = ["Matemáticas", "Álgebra", "Geometría"]
        niveles = ["Fácil", "Intermedio", "Difícil"]
        
        for modulo in modulos:
            tk.Radiobutton(self.root, text=modulo, variable=self.modulo, value=modulo).pack(anchor=tk.W)
        
        tk.Label(self.root, text="Elige un nivel").pack(pady=10)
        
        for nivel in niveles:
            tk.Radiobutton(self.root, text=nivel, variable=self.nivel, value=nivel).pack(anchor=tk.W)
        
        tk.Button(self.root, text="Comenzar", command=self.iniciar_juego).pack(pady=20)

    def iniciar_juego(self):
        modulo = self.modulo.get()
        nivel = self.nivel.get()
        
        if not modulo or not nivel:
            messagebox.showwarning("Error", "Debes seleccionar un módulo y un nivel")
            return
        
        banco_preguntas = cargar_preguntas(ruta_archivo)
        self.preguntas = seleccionar_preguntas(banco_preguntas, modulo, nivel)
        
        self.tiempo_limite = {"Fácil": 15, "Intermedio": 20, "Difícil": 30}[nivel]
        
        self.vidas = 3
        self.puntuacion = 0
        self.pregunta_actual = 0
        
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        if self.pregunta_actual < len(self.preguntas):
            pregunta = self.preguntas.iloc[self.pregunta_actual]
            
            self.limpiar_pantalla()
            
            tk.Label(self.root, text=pregunta['Pregunta'], font=("Helvetica", 14)).pack(pady=20)
            opciones = ['Opción A', 'Opción B', 'Opción C', 'Opción D']
            
            self.respuesta_usuario = tk.StringVar()
            
            for opcion in opciones:
                tk.Radiobutton(self.root, text=pregunta[opcion], variable=self.respuesta_usuario, value=opcion).pack(anchor=tk.W)
            
            self.inicio_tiempo = time.time()
            tk.Button(self.root, text="Responder", command=lambda: self.verificar_respuesta(pregunta['Respuesta Correcta'])).pack(pady=20)
        else:
            self.mostrar_resultado()

    def verificar_respuesta(self, respuesta_correcta):
        tiempo_transcurrido = time.time() - self.inicio_tiempo
        
        if tiempo_transcurrido > self.tiempo_limite:
            messagebox.showwarning("Tiempo agotado", f"Tiempo agotado. Tenías {self.tiempo_limite} segundos para responder.")
            self.vidas -= 1
        elif self.respuesta_usuario.get() == respuesta_correcta:
            messagebox.showinfo("Correcto", "¡Correcto!")
            self.puntuacion += 1
        else:
            messagebox.showerror("Incorrecto", f"Incorrecto. La respuesta correcta era: {respuesta_correcta}")
            self.vidas -= 1
        
        self.pregunta_actual += 1
        
        if self.vidas > 0:
            self.mostrar_pregunta()
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        self.limpiar_pantalla()
        
        tk.Label(self.root, text="Juego Terminado", font=("Helvetica", 16)).pack(pady=20)
        tk.Label(self.root, text=f"Tu puntuación: {self.puntuacion}").pack(pady=5)
        
        if self.vidas == 0:
            tk.Label(self.root, text="Has perdido todas tus vidas").pack(pady=5)
        else:
            tk.Label(self.root, text="¡Felicidades! Has completado todas las preguntas").pack(pady=5)
        
        usuario['puntuacion'] = self.puntuacion
        
        tk.Button(self.root, text="Volver al Menú Principal", command=self.crear_menu_principal).pack(pady=10)

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Juego(root)
    root.mainloop()
