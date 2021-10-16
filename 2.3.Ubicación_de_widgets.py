from tkinter import *
root=Tk()
root.title("posicionar")
root.geometry("400x200")#tamaño de ventana 
def sauludar():
    print("hola te saludo")
def minimizar():
    root.iconify()#funcion para minimizar la pantalla
buton1 = Button(root,text="haz click aqui para saludar",command= sauludar)
buton1.place(x=200, y=50)#le damos ubicacion al boton
buton2 = Button(root,text="haz click aqui para Minimizar",command = minimizar)
buton2.place(x=200, y=100)
etiqueta=Label (root,text="Saludar desde aqui")
etiqueta.place(x=30, y=50)
etiqueta1=Label (root,text="Minimizar desde aqui ")
etiqueta1.place(x=30, y=100)
root.mainloop()
