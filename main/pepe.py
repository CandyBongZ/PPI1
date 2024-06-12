import pandas as pd
import random
import time
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class JuegoDePreguntas:
    def __init__(self, master):
        self.master = master
        self.master.resizable(False, False)
        self.master.title("Juego de Preguntas")
        self.usuario = None
        self.puntuacion = 0
        self.vidas = 3
        self.pregunta_actual = 0
        self.tiempo_limite = 0
        self.inicio_tiempo = 0
        self.imagenes = []  # Lista para guardar las imágenes

        # Cargar el archivo Excel
        ruta_archivo = r"C:\python\ppi\main\preguntas.xlsx"
        self.df = pd.read_excel(ruta_archivo)

        self.mostrar_inicio()

    def foto(self):
        self.master.geometry("650x585")
        ruta_imagen = r"C:\python\ppi\main\imagen.png"
        imagen = Image.open(ruta_imagen)
        self.imagen_fondo = ImageTk.PhotoImage(imagen)
        label = tk.Label(self.master, image=self.imagen_fondo)
        label.image = self.imagen_fondo  # Guardar una referencia a la imagen
        label.place(x=0, y=0, relwidth=1, relheight=1)


    def logo(self):
        ruta_imagen = r"C:\python\ppi\main\logoj.png"
        imagen = Image.open(ruta_imagen)
        imagen = imagen.convert("RGBA")  # Convertir la imagen a RGBA para manejar la transparencia
        datos = imagen.getdata()  # Obtener los datos de la imagen

    

        nuevos_datos = []
        for item in datos:
            # Cambiar todos los píxeles blancos (también los parcialmente transparentes) a transparentes
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                nuevos_datos.append((255, 255, 255, 0))
            else:
                nuevos_datos.append(item)
                
        imagen.putdata(nuevos_datos)
        self.imagen_logo = ImageTk.PhotoImage(imagen)
        label = tk.Label(self.master, image=self.imagen_logo, bg='white')
        label.image = self.imagen_logo
        label.place(relx=0.5, rely=0.32, anchor='center')  # Colocar el logo en el centro de la ventana  # Colocar el logo en el centro de la ventana  # Colocar el logo en el centro de la ventana 
    def logotrofeo(self):
        ruta_imagen = r"C:\python\ppi\main\logotrofeo.png"
        imagen = Image.open(ruta_imagen)
        imagen = imagen.resize((250, 250))
        imagen = imagen.convert("RGBA")  # Convertir la imagen a RGBA para manejar la transparencia
        datos = imagen.getdata()  # Obtener los datos de la imagen
        

    

        nuevos_datos = []
        for item in datos:
            # Cambiar todos los píxeles blancos (también los parcialmente transparentes) a transparentes
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                nuevos_datos.append((255, 255, 255, 0))
            else:
                nuevos_datos.append(item)
                
        imagen.putdata(nuevos_datos)
        self.imagen_logo = ImageTk.PhotoImage(imagen)
        label = tk.Label(self.master, image=self.imagen_logo, bg='white')
        label.image = self.imagen_logo
        label.place(relx=0.5, rely=0.32, anchor='center')
    
    def mostrar_inicio(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.foto()
        self.logo()
    
        label1 = tk.Label(self.master, text="ANTIVIRUS PARA LA DESERCIÓN", bd=0, bg='white')
        label1.place(relx=0.5, rely=0.65, anchor='center')
    
        label2 = tk.Label(self.master, text="Por favor, ingresa tu nombre de usuario:", bd=0, bg='white')
        label2.place(relx=0.5, rely=0.73, anchor='center')
    
        self.entrada_usuario = tk.Entry(self.master)
        self.entrada_usuario.place(relx=0.5, rely=0.8, anchor='center')
    
        ruta_imagen_boton = r"C:\python\ppi\main\iniciar.png"  # Reemplaza esto con la ruta a tu imagen
        imagen_boton = Image.open(ruta_imagen_boton)
        imagen_boton = imagen_boton.resize((120, 55))  # Cambiar el tamaño de la imagen a 50x50
        self.imagen_boton = ImageTk.PhotoImage(imagen_boton)
        button = tk.Button(self.master, image=self.imagen_boton, command=self.iniciar_sesion, bd=0, bg='white')  # bg='white' hace que el botón sea del mismo color que el fondo
        button.image = self.imagen_boton  # Guardar una referencia a la imagen
        button.place(relx=0.5, rely=0.9, anchor='center')
    
        self.centrar_ventana()

    def iniciar_sesion(self):
        self.usuario = self.entrada_usuario.get()
        if self.usuario:
            self.mostrar_menu()

    def mostrar_menu(self):
        
        self.master.geometry("650x500")  # Establecer el tamaño de la ventana a 500x500

        for widget in self.master.winfo_children():
            widget.destroy()
        self.foto()
        self.logo()

        label1 = tk.Label(self.master, text="ANTIVIRUS PARA LA DESERCIÓN", bd=0, bg='white')
        label1.place(relx=0.5, rely=0.65, anchor='center')

        ruta = r"C:\python\ppi\main\jugar.png"
        pepito = self.letras(ruta)  
        botonjugar = tk.Button(self.master, image=pepito, text="1. Jugar", command=self.mostrar_opciones_juego, bd=0, bg='white')
        botonjugar.pack(pady=10)
        botonjugar.place(relx=0.3, rely=0.85, anchor='center')
        
        ruta2 = r"C:\python\ppi\main\perfil.png"
        pepe = self.letras(ruta2)
        botonperfil = tk.Button(self.master, image=pepe, text="2. Perfil de usuario", command=self.mostrar_perfil, bd=0, bg='white')
        botonperfil.pack(pady=10)
        botonperfil.place(relx=0.5, rely=0.85, anchor='center')
        
        ruta3 = r"C:\python\ppi\main\salir.png"
        pepote = self.letras(ruta3)
        botonsalir = tk.Button(self.master, image=pepote, text="3. Salir", command=self.salir, bd=0, bg='white')
        botonsalir.pack(pady=10)
        botonsalir.place(relx=0.7, rely=0.85, anchor='center')
  

        self.centrar_ventana()  # Centrar la ventana en la pantalla


    def letras(self, ruta):
        ruta_imagen_boton = ruta
        imagen_boton = Image.open(ruta_imagen_boton)
        imagen_boton = imagen_boton.resize((70, 90))
        imagen_boton_tk = ImageTk.PhotoImage(imagen_boton)
        self.imagenes.append(imagen_boton_tk)  # Guarda una referencia a la imagen
        return imagen_boton_tk

    def mostrar_opciones_juego(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.foto()
        self.logo()

        label3 = tk.Label(self.master, text="Selecciona un módulo:")
        label3.place(relx=0.5, rely=0.6, anchor='center')
        self.modulo = tk.StringVar(value="Matemáticas")
        opciones_modulo = ["Matemáticas", "Álgebra", "Geometría"]
        combo = ttk.Combobox(self.master, values=opciones_modulo)
        combo.place(relx=0.5, rely=0.65, anchor='center')


        tk.Label(self.master, text="Selecciona un nivel:").place(relx=0.5, rely=0.7, anchor='center')
        self.nivel = tk.StringVar(value="Fácil")
        opciones_nivel = ["Fácil", "Medio", "Difícil"]
        combo = ttk.Combobox(self.master, values=opciones_nivel)
        combo.place(relx=0.5, rely=0.75, anchor='center')


        tk.Button(self.master, text="Comenzar", command=self.iniciar_juego).place(relx=0.5, rely=0.8, anchor='center')

    def iniciar_juego(self):
        self.puntuacion = 0
        self.vidas = 3
        self.pregunta_actual = 0

        modulo_seleccionado = self.modulo.get()
        nivel_seleccionado = self.nivel.get()
        if nivel_seleccionado == "Fácil":
            self.tiempo_limite = 15
        elif nivel_seleccionado == "Medio":
            self.tiempo_limite = 20
        else:
            self.tiempo_limite = 30

        self.preguntas = self.seleccionar_preguntas(self.df, modulo_seleccionado, nivel_seleccionado)
        self.mostrar_pregunta()

    def seleccionar_preguntas(self, df, modulo, nivel, num_preguntas=5):
        preguntas_filtradas = df[(df['Módulo'] == modulo) & (df['Nivel'] == nivel)]
        preguntas_seleccionadas = preguntas_filtradas.sample(n=num_preguntas)
        return preguntas_seleccionadas

    def mostrar_pregunta(self):
        if self.pregunta_actual < len(self.preguntas):
            pregunta = self.preguntas.iloc[self.pregunta_actual]
            self.inicio_tiempo = time.time()

            for widget in self.master.winfo_children():
                widget.destroy()
            self.foto()

            letrajugar = tk.Label(self.master, text=pregunta['Pregunta']).pack(pady=10)
            opciones = {'A': pregunta['Opción A'], 'B': pregunta['Opción B'], 'C': pregunta['Opción C'], 'D': pregunta['Opción D']}
            self.respuesta_usuario = tk.StringVar()
        

            for clave, valor in opciones.items():
                tk.Radiobutton(self.master, text=valor, variable=self.respuesta_usuario, value=valor).pack(pady=2)

            respuesta_correcta = pregunta['Respuesta Correcta']
            if respuesta_correcta not in opciones.values():
                messagebox.showwarning("Error", "La respuesta correcta no coincide con ninguna de las opciones.")
                self.vidas = 0
                self.mostrar_resultado()
                return

            tk.Button(self.master, text="Responder", command=lambda: self.verificar_respuesta(respuesta_correcta)).pack(pady=10)
        else:
            self.mostrar_resultado()

    def verificar_respuesta(self, respuesta_correcta):
        tiempo_transcurrido = time.time() - self.inicio_tiempo

        if tiempo_transcurrido > self.tiempo_limite:
            messagebox.showwarning("Tiempo agotado", f"Tiempo agotado. Tenías {self.tiempo_limite} segundos para responder.")
            self.vidas -= 1
        elif self.respuesta_usuario.get().lower() == str(respuesta_correcta).lower():
            messagebox.showinfo("Correcto", "¡Correcto!")
            self.puntuacion += 1
        else:
            messagebox.showwarning("Incorrecto", "Respuesta incorrecta.")
            self.vidas -= 1

        self.pregunta_actual += 1

        if self.vidas > 0:
            self.mostrar_pregunta()
        else:
            self.mostrar_resultado()

    def mostrar_resultado(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.foto()

        tk.Label(self.master, text=f"Juego terminado. Tu puntuación es: {self.puntuacion}").pack(pady=10)
        tk.Button(self.master, text="Volver al menú", command=self.mostrar_menu).pack(pady=10)

    def mostrar_perfil(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        self.foto()
        self.logotrofeo()

        tk.Label(self.master, text=f"Perfil de usuario: {self.usuario}").place(relx=0.5, rely=0.7, anchor='center')
        tk.Label(self.master, text=f"Puntuación: {self.puntuacion}").place(relx=0.5, rely=0.75, anchor='center')
        tk.Button(self.master, text="Volver al menú", command=self.mostrar_menu).place(relx=0.5, rely=0.8, anchor='center')

    def salir(self):
        self.usuario = None
        self.mostrar_inicio()

    def centrar_ventana(self):
        self.master.update_idletasks()  # Actualizar la ventana para obtener las dimensiones finales
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
        position_right = int(self.master.winfo_screenwidth()/2 - window_width/2)
        position_down = int(self.master.winfo_screenheight()/2 - window_height/2)
        self.master.geometry("+{}+{}".format(position_right, position_down))

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoDePreguntas(root)
    root.mainloop()

    

