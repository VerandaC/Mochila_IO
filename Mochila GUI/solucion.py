from tkinter import *
from tkinter.scrolledtext import ScrolledText
# import tkinter
from nuevo_problema import *
from menu_problema import *

a=("a","b","c","d","e","1","2","3","f","4","5","6","g","7","8","9","3","f","4","5","6","g","7","8","9")
class solucion:
    def __init__(self,sol,cant,util,peso):
        # Creacion de la ventana solucion
        self.sol=sol
        self.cant=cant
        self.util=util
        self.peso=peso
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


        self.lista = Listbox(solucion)
        
        b1=Button(self.lista, text="anterior")
        # b1.grid(column=0,row=4,padx=4,pady=4)
        b2=Button(self.lista, text="siguiente")
        # b2.grid(column=0,row=4,padx=4,pady=4)

        #Llamada al menu problema
        menu_problema(solucion)
        
       

        #Creacion de la funcion que genera las matrices solucion
        def soluciones():
            etiqueta_sol=Label(self.lista, text=f'Solucion: {1} \nUtilidad total de las soluciones: {self.util} \nProducto         Cantidad           Peso           Utilidad')
            matriz = Text(self.lista)
            # self.lista.insert("end","\n \n \n")
            genera_matriz(a,matriz)
            # self.lista.insert("end","\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
            etiqueta_peso =Label(self.lista,text=f'Peso total utilidad: {self.peso}')
            etiqueta_sol.pack()
            matriz.pack()
            etiqueta_peso.pack()
            b1.pack(side=LEFT)
            b2.pack(side=RIGHT)
                
                

        # Creacion de la funcion que genera la matriz 
        def genera_matriz(a,matriz):
            s=0
            for r in range(0,self.cant):
                for c in range(0,4):
                    b=a[s]
                    s+=1
                    celda = Label(matriz,text=b, width=8)
                    celda.grid(padx=5, pady=5, row=r, column=c)
                    celda.config(fg="white",    # letra
                        bg="skyblue",   # caja
                        font=("Verdana",12))
        
        soluciones()
        
        self.lista.pack(fill="both",expand=True)    

        solucion.mainloop()

# solucion=solucion()