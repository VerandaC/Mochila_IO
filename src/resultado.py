from tkinter import *
from .nuevo_problema import *
from .menu_problema import *

class resultado:
    def __init__(self,cant, soluciones, pesos, utilidad):
       
        # Creacion de la ventana solucion
        self.soluciones=soluciones
        self.cant=cant
        self.utilidad=utilidad
        self.pesos=pesos
        print(self.soluciones)
        print(self.cant)
        print(self.utilidad)
        print(self.pesos)
        self.indice = 0
        solucion = Tk()
        self.x=420
        self.y=250
        if(self.cant >=2 and self.cant<=7):
            self.x = self.x + (1*self.cant )
            self.y = self.y + (20*self.cant )
        else:
            self.x = self.x + (2*self.cant )
            self.y = self.y + (30*self.cant )

        self.x1=solucion.winfo_screenwidth()// 2 - self.x // 2
        self.y1=solucion.winfo_screenheight()// 2 - self.y // 2


        solucion.geometry(f'{self.x}x{self.y}+{self.x1}+{self.y1}')
        solucion.resizable(0,0)
        solucion.title("Asignacion caso mochila")
        solucion.config(bg="linen")

        def sgte_solucion():
            self.indice += 1
            print_solucion()
            # if self.indice == len(self.soluciones):

        def ant_solucion():
            self.indice -=1
            print_solucion()


        # self.lista = Listbox(solucion)
        
        self.b1=Button(solucion, text="anterior",bg="lavender", command=ant_solucion)
        self.b2=Button(solucion, text="siguiente",bg="lavender", command=sgte_solucion)

        #Llamada al menu problema
        menu_problema(solucion)
        
       

        #Creacion de la funcion que genera las matrices solucion
        def soluciones():
            etiqueta_sol=Label(solucion, text=f'Solucion: {1} \nUtilidad total de las soluciones: {self.utilidad} \nProducto         Cantidad           Peso           Utilidad',bg="linen")
            matriz = Frame(solucion)
            genera_matriz(matriz)
            self.etiqueta_peso =Label(solucion,bg="linen")
            etiqueta_sol.pack()
            matriz.pack()
            self.etiqueta_peso.pack()
            self.b1.pack(side=LEFT,padx=65,pady=15)
            self.b2.pack(side=RIGHT,padx=70,pady=15)

        # Creacion de la funcion que genera la matriz 
        def genera_matriz(matriz):
            self.matriz_sol = []
            for r in range(0,self.cant):
                fila = []
                for c in range(0,4):
                    celda = Entry(matriz, width=8)
                    celda.grid(padx=5, pady=5, row=r, column=c)
                    celda.config(fg="white",    # letra
                                bg="skyblue",   # caja
                                font=("Verdana",12))
                    fila.append(celda)
                self.matriz_sol.append(fila)

        def print_solucion():
            sol = self.soluciones[self.indice]
            print(sol)
            # self.etiqueta_peso.config(text=f'Peso total: {self.pesos[self.indice]}')
            for fila_sol, fila_mat in zip(sol, self.matriz_sol):
                for dato, celda in zip(fila_sol, fila_mat):
                    celda.delete(0, len(celda.get()))
                    celda.insert(0, dato)

        soluciones()
        print_solucion()

        solucion.mainloop()

