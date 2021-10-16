import tkinter as tk
from tkinter import ttk
root = tk.Tk()
def seleccionar(opcion):
    print(opcion)
ttk.Button(root,text= "Python", command=lambda: seleccionar("python")).pack()
ttk.Button(root,text= "Javascrip", command=lambda: seleccionar("JavaScript")).pack()
ttk.Button(root,text= "Java", command=lambda: seleccionar("Java")).pack()
root.mainloop()
