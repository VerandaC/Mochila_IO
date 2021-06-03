from tkinter import *
dic={'lis1':['a'],'lis2':['a','b'],'lis3':['a','b','c']}

class prueba:
    def __init__(self):
        
        ventana = Tk()
        ventana.geometry('500x500')
        self.b1=Button(ventana, text="anterior")
        self.b2=Button(ventana, text="siguiente")
        def ocultar_anterior():
                self.b1.place_forget()
        def ocultar_siguiente():
                self.b2.place_forget()
        def ocultar_botones():
                self.b1.place_forget()
                self.b2.place_forget()
        

        def verificar(lis):
            if(len(lis)==1):
                print(len(lis))
                ocultar_botones()
            elif(lis[2]):
                ocultar_anterior()
            elif(lis[-1]):
                ocultar_siguiente()



        
        print(len(dic['lis1']))
        print(dic['lis1'][0])
        self.b1.config(command=verificar(dic['lis1']))
        self.b1.place(x=20, y=200)
        self.b2.config(command=verificar(dic['lis1']))
        self.b2.place(x=100, y=200)


        
                
        lis =Listbox(ventana)
        lis.insert(1,dic['lis1'])
        lis.insert(2,dic['lis1'])
        lis.insert(3,dic['lis1'])
        lis.pack(side=TOP)


        ventana.mainloop()

v=prueba()  


