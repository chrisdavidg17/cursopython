from cProfile import label
import tkinter
from tkinter import ttk

window = tkinter.Tk()
label = tkinter.Label(window, text='Lista para elegir')
label.pack()

selecccion = tkinter.StringVar()
sel1 = ttk.Radiobutton(window, text='Primera Eleccion', value = 1, variable=selecccion)
sel2 = ttk.Radiobutton(window, text='Segunda Eleccion', value = 2, variable=selecccion)
sel3 = ttk.Radiobutton(window, text='Tercera Eleccion', value = 3, variable=selecccion)
sel4 = ttk.Radiobutton(window, text='Cuarta Eleccion', value = 4, variable=selecccion)
sel1.pack()
sel2.pack()
sel3.pack()
sel4.pack()

def reset(event):
    selecccion.set(None)

reserbuttom = ttk.Button(window, text = 'Reset')
reserbuttom.pack()
reserbuttom.bind('<Button-1>', reset)
window.mainloop()



