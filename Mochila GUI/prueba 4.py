import tkinter as tk


# from tkinter.constants import TOP
# from typing import Text
# class prueba:
#     def __init__(self):
#         ventana = tk.Tk()
#         ventana.geometry('200x200')
#         def cambiar_indice(n):
#             pass
        
#         def ocultar_botones(b1,b2):
#                 if b1.winfo_ismapped():
#                     b1.place_forget()
#                     b2.configure(text="Mostrar texto")
#                 else:
#                     b1.place(x=70, y=50)
#                     b2.configure(text="Ocultar texto")
                    
#         # b1 = tk.Text(ventana, text="mostrar texto", command=btn_hide, fg="black", width=10)
#         # b1.place(x=70, y=50)
#         # b2 = tk.Button(ventana, text="Ocultar texto", command=btn_hide, fg="black", width=10)
#         # b2.place(x=50, y=90)

#         # ventana.mainloop()
    
#         lis1=("a")
#         lis2=("a","b")
#         lis3=("a","b","c")
#         lis4=("a","b","c","d","e")
#         lis=tk.Listbox(ventana)
#         lis.insert(1,lis1)
#         lis.insert(2,lis2)
#         lis.insert(3,lis3)
#         lis.pack(side=TOP)

#         b1=tk.Button(ventana, text="anterior",command=cambiar_indice(lis1))
#         b1.place(x=20, y=90)
#         b2=tk.Button(ventana, text="siguiente",command=cambiar_indice(lis1))
#         b2.place(x=100, y=90)

#         self.respuesta = tk.Listbox(ventana)
#         #self.respuesta.insert(lis)


#         def ocultar_botones():
#             b1.place_forget()
#             b2.place_forget()

#         def mostrar_sig():
#             b1.place_forget
#             b2.place(x=100, y=90)

#         def mostrar_ant():
#             b1.place(x=20, y=90)
#             b2.place_forget

#         def mostrar_botones():
#             b1.place(x=20, y=90)
#             b2.place(x=100, y=90)

#         def cambiar_indice(lis):
#             if(len(lis)==1):
#                 ocultar_botones(b1,b2)
#             if(len(lis)==2):
#                 if(lis[0]):
#                     mostrar_sig()
#                 else:
#                     mostrar_ant()
#             if(len(lis)>2):
#                 if(lis[0]):
#                     mostrar_sig()
#                 else:
#                     if(lis[len(lis)-1]):
#                         mostrar_ant()
#                     else:
#                         mostrar_botones()
        
        

#         ventana.mainloop()

# v=prueba()    

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.label=tk.Label(self.root,
                           text = "Label")
       self.buttonForget = tk.Button(self.root,
                          text = 'Click to hide Label',
                          command=lambda: self.label.pack_forget())
       self.buttonRecover = tk.Button(self.root,
                          text = 'Click to show Label',
                          command=lambda: self.label.pack())       
       
       self.buttonForget.pack()
       self.buttonRecover.pack()
       self.label.pack(side="bottom")
       self.root.mainloop()

   def quit(self):
       self.root.destroy()
        
app = Test()