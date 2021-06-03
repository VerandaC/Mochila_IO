from tkinter import *
from tkinter.scrolledtext import ScrolledText
# from tkinter import scrolledtext as st
# from principal import principal
from menu_problema import menu_problema
from solucion import solucion


class ingreso_datos:
    def __init__(self,cant,cap):
        self.cant = cant
        self.cap = cap
        # a=nuevo_problema

        # Creacion de la ventana problema
        self.x=420
        self.y=250
        self.ventana = Tk()
        if(self.cant >=2 and self.cant<=7):
            self.x = self.x + (1*self.cant )
            self.y = self.y + (20*self.cant )
        else:
            self.x = self.x + (2*self.cant )
            self.y = self.y + (30*self.cant )

        self.x1=self.ventana.winfo_screenwidth()// 2 - self.x // 2
        self.y1=self.ventana.winfo_screenheight()// 2 - self.y // 2


        self.ventana.geometry(f'{self.x}x{self.y}+{self.x1}+{self.y1}')
        self.ventana.resizable(0,0)
        self.ventana.title("Asignacion caso mochila")
        
      

        #Llamada al menu problema
        menu_problema(self.ventana) # Veremos  
         

        #Creacion del marco etiquetas
        self.etiquetas_problema = Frame(self.ventana)
        self.etiquetas_datos()
        self.etiquetas_problema.pack(side = TOP)

 

        # Creacion del marco matriz
        self.matriz_problema = Listbox(self.ventana)
        self.genera_matriz()
        self.matriz_problema.pack()

        

        #Creacion del marco botones
        self.botones= Frame(self.ventana)
        self.botones.pack(side=BOTTOM)

        #Boton cancelar
        self.cancelar=Button(self.botones, text="Cancelar",command=self.cancelar)
        self.cancelar.grid(column=0,row=2,padx=4,pady=4)
        

        #Boton correr
        # self.ok=Button(self.botones, text="Correr",command=self.generar_ventana_solucion)
        self.ok=Button(self.botones, text="Correr",command=self.get_datos_tabla)
        self.ok.grid(column=5,row=2,padx=4,pady=4)

        


        self.ventana.mainloop()

# Creacion de la funcion que genera la matriz 
    def genera_matriz(self):
        self.matriz = []
        for r in range(0,self.cant):
            fila = []
            for c in range(0, 3):
                celda = Entry(self.matriz_problema, width=12)
                celda.grid(padx=5, pady=5, row=r, column=c)
                celda.insert(0, '({}, {})'.format(r, c))
                celda.config(fg="white",    # letras
                            bg="skyblue3",   # fondo
                            font=("Verdana",12))
                fila.append(celda)
            self.matriz.append(fila)

    
    def generar_ventana_solucion(self):
        # self.ventana.destroy()
        print("self cantidad ",self.cant)
        solucion(4,self.cant,4,8)
        
    
    
    
    def get_datos_tabla(self):
        nombres = []
        pesos = []
        utilidades = []
        for fila in self.matriz:
            nombres.append(fila[0].get())
            pesos.append(fila[1].get())
            utilidades.append(fila[2].get())

        print('Nombres: ', nombres)
        print('Pesos: ', pesos)
        print('Utilidades: ', utilidades)
        print('SOLUCION DEL PROBLEMA')
        self.generar_ventana_solucion()

#Creacion de otras Ventanas
    def cancelar(self):
        self.ventana.destroy()


    def etiquetas_datos(self):

        self.etq_capacidad=Label(self.etiquetas_problema, text=f'Capacidad de la mochila : {self.cap}')
        self.etq_capacidad.grid(column=0,row=0,padx=4,pady=4)
        
        self.etq_cantidad=Label(self.etiquetas_problema, text=f'Cantidad de articulos : {self.cant}')
        self.etq_cantidad.grid(column=0,row=1,padx=4,pady=4)

        self.etq_datos=Label(self.etiquetas_problema, text="      Articulos                Peso                     Utilidad")
        self.etq_datos.grid(column=0,row=2,padx=4,pady=4)

    