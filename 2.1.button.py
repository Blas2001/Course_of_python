from tkinter import *
import time
root = Tk()
root.title("Mi primera ventana")#titulo de ventana 
root.geometry("500x300")#tamaño de la ventana
Button1 = Button(root, text="minimizar", command = root.iconify,bg="blue")
Button1.pack(side=RIGHT)#le da una pisición centrica
def imprimir():
    label1= Label(root, text="imprimiendo")
    label1.pack()
Button2 = Button(root,text="Imprimir",command = imprimir,bg="red")
Button2.pack(side=LEFT)

root.mainloop()
