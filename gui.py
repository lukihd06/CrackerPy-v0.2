#! /usr/bin/python
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Tkinter import *
import brute

iterationSpeedV = 189966.24615402461

window = Tk()

window.title("CrackerPy v0.1")
window.geometry("1200x900")

lblComplex = Label(window, text="Complexite du mot de passe")

possibilities=[]

fig = Figure(figsize=(9,5), dpi=100)
curve = fig.add_subplot(111)
curve.plot([1,2,3,4,5,6,7,8,9,10], [10,9,8,7,6,5,4,3,2,1])

canvas = FigureCanvasTkAgg(fig)
canvas.show
canvas.get_tk_widget().grid(column=2, row=6)

def AddLowerCase():
    global possibilities
    if chkLowerCase and not set(brute.lowerCase).issubset(possibilities):
        possibilities += brute.lowerCase
    else:
        for p in brute.lowerCase: 
            if p in possibilities: 
                possibilities.remove(p)

def AddUpperCase():    
    global possibilities
    if chkUpperCase and not set(brute.upperCase).issubset(possibilities):
        possibilities += brute.upperCase
    else:
        for p in brute.upperCase: 
            if p in possibilities: 
                possibilities.remove(p)

def AddNumber():    
    global possibilities
    if chkNumber and not set(brute.number).issubset(possibilities):
        possibilities += brute.number
    else:
        for p in brute.number: 
            if p in possibilities: 
                possibilities.remove(p)

def AddSpecial():    
    global possibilities
    if chkSpecial and not set(brute.special).issubset(possibilities):
        possibilities += brute.special
    else:
        for p in brute.special: 
            if p in possibilities: 
                possibilities.remove(p)

varLowerCase = BooleanVar()
varUpperCase = BooleanVar()
varNumber = BooleanVar()
varSpecial = BooleanVar()

chkLowerCase = Checkbutton(window, text='minuscule', var=varLowerCase, command=AddLowerCase)
chkUpperCase = Checkbutton(window, text='majuscule', var=varUpperCase, command=AddUpperCase)
chkNumber = Checkbutton(window, text='chiffre', var=varNumber, command=AddNumber)
chkSpecial = Checkbutton(window, text='special', var=varSpecial, command=AddSpecial)

lblIterationSpeed = Label(window, text="Capacite de calcul d'iterations par secondes")

iterationsPerSeconds = 0

def StartTest():
    iterationsPerSeconds = brute.howManyIterationPerSeconds()
    Label(window, text=iterationsPerSeconds).grid(column=2 ,row=1, sticky=W)

btnQuit = Button(window, text="Quitter", command=window.quit)    
btnStartTest = Button(window, text="Demarrer le test", command=StartTest)

lblComplex.grid(column=0 ,row=0, sticky=W)

chkLowerCase.grid(column=0 ,row=1, sticky=W)
chkUpperCase.grid(column=0 ,row=2, sticky=W)
chkNumber.grid(column=0 ,row=3, sticky=W)
chkSpecial.grid(column=0 ,row=4, sticky=W)

lblIterationSpeed.grid(column=2 ,row=0, sticky=W)

btnQuit.grid(column=1 ,row=5, sticky=W)
btnStartTest.grid(column=2 ,row=5, sticky=W)

window.mainloop()