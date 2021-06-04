from tkinter import *
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
        solucion.config(bg="linen")


        # self.lista = Listbox(solucion)
        
        b1=Button(solucion, text="anterior",bg="lavender")
        b2=Button(solucion, text="siguiente",bg="lavender")

        #Llamada al menu problema
        menu_problema(solucion)
        
       

        #Creacion de la funcion que genera las matrices solucion
        def soluciones():
            etiqueta_sol=Label(solucion, text=f'Solucion: {1} \nUtilidad total de las soluciones: {self.util} \nProducto         Cantidad           Peso           Utilidad',bg="linen")
            matriz = Frame(solucion)
            genera_matriz(a,matriz)
            etiqueta_peso =Label(solucion,text=f'Peso total utilidad: {self.peso}',bg="linen")
            etiqueta_sol.pack()
            matriz.pack()
            etiqueta_peso.pack()
            b1.pack(side=LEFT,padx=65,pady=15)
            b2.pack(side=RIGHT,padx=70,pady=15)
                
                

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
        

        solucion.mainloop()

