import tkinter
from tkinter import W, ttk
from tkinter.tix import COLUMN

window = tkinter.Tk()

window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=3)
window.columnconfigure(3, weight=3)

label = tkinter.Label(window, text='Ejercio de GUI')
label.grid(column=0, row=0, sticky=tkinter.W)

selecciones=tkinter.StringVar()
r1=ttk.Radiobutton(window, text='Primera', value= 1, variable=selecciones)
r2=ttk.Radiobutton(window, text='Segunda', value= 2, variable=selecciones)
r1.grid(column=0, row=1, sticky=tkinter.W)
r2.grid(column=0, row=2, sticky=tkinter.W)

selecciones1=tkinter.StringVar()
r3=ttk.Radiobutton(window, text='A', value= 1, variable=selecciones1)
r4=ttk.Radiobutton(window, text='B', value= 2, variable=selecciones1)
r3.grid(column=1, row=1, sticky=tkinter.W)
r4.grid(column=1, row=2, sticky=tkinter.W)

selecciones2=tkinter.StringVar()
r5=ttk.Radiobutton(window, text='Primera', value= 1, variable=selecciones2)
r6=ttk.Radiobutton(window, text='Segunda', value= 2, variable=selecciones2)
r5.grid(column=2, row=1, sticky=tkinter.W)
r6.grid(column=2, row=2, sticky=tkinter.W)

def salir(event):
    window.quit()

reserbuttom = ttk.Button(window, text = 'Salir')
reserbuttom.grid(column=1, row=3, sticky=tkinter.W)
reserbuttom.bind('<Button-1>', salir)

window.mainloop()