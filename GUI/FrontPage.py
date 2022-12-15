from tkinter import *
from Backend.Projekt import Projekt

pro1 = Projekt("","","","","")
#pro1.CreateProjekt()
#pro1.ReadProjekts()


class GUI:
    window = Tk()
    window.geometry('300x500')
    listOfProjekts = Listbox(window)

    for item in pro1.ReadProjekts():
        listOfProjekts.insert('end',item.projektnavn)

    listOfProjekts.pack()

    window.mainloop()
