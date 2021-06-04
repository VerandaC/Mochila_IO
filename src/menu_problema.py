from tkinter import*
from tkinter import filedialog as fd
import os
# from .nuevo_problema import nuevo_problema

class menu_problema:
    def __init__(self,v):
        print('NOMBRE VENTANA:', v)
        #Creacion de otras Ventanas
        def nuevo():
            v.destroy()
            # nuevo=nuevo_problema()

        def guardar():
            nombre_archivo=fd.asksaveasfilename(initialdir = os.getcwd() ,title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
            if nombre_archivo!='':
                archivo=open(nombre_archivo + ".txt", "w", encoding="utf-8")
                archivo.write(self.scrolledtext1.get("1.0", END))
                archivo.close()
               

        def recuperar():
            nombre_archivo=fd.askopenfilename(initialdir = os.getcwd() ,title = "Seleccione archivo",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
            if nombre_archivo!='':
                archivo=open(nombre_archivo, "r", encoding="utf-8")
                contenido=archivo.read()
                archivo.close()
                self.scrolledtext1.delete("1.0", END) 
                self.scrolledtext1.insert("1.0", contenido)

        # Creacion de la barra de menus
        barra_menu = Menu(v)

        # Creacion de menus
        archivo = Menu(barra_menu)
        exportar = Menu(barra_menu)
        ayuda = Menu(barra_menu)

        # Creacion de los comandos para menu archivo
        archivo.add_command(label="Nuevo Problema", command=nuevo)
        archivo.add_command(label="Cargar problema",command=recuperar)
        archivo.add_command(label="Guardar", command=guardar)
        archivo.add_separator()
        archivo.add_command(label="Salir")

        # Creacion de los comandos para menu exportar
        exportar.add_command(label="Como DOC")
        exportar.add_command(label="Como PDF")
        exportar.add_command(label="Como JPG")

        # Creacion de los comandos para menu ayuda
        ayuda.add_command(label="Manual de uso")
        ayuda.add_command(label="Acerca de")

        # Agregar los menus a la barra de menus
        barra_menu.add_cascade(label="Archivo", menu=archivo)
        barra_menu.add_cascade(label="Exportar", menu=exportar)
        barra_menu.add_cascade(label="Ayuda", menu=ayuda)
        
        # Agregar la barra a principal
        v.config(menu=barra_menu)

        