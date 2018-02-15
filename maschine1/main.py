#!/usr/bin/env python
# -*- coding: utf8 -*-
from Tkinter import *
import tkFont
import time
import write_blue
import write_red
import write_purple
import write_yellow

#Definition des Programmes und Übergabe des dazugehörigen Objekts

class Program(object):

    #Erzeugung des Fensters (maximiert) + Festlegung der Geometrie beim Umschalten 
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='700x400+50+50'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        #Festlegung der Taste zum Umschalten des Fensters
        master.bind('<F11>', self.toogle_geom)
        
        # Erzeugung des Gridlayouts
        global frame
        frame=Frame(root)
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        frame.grid(row=0, column=0, sticky=N+S+E+W)
        grid=Frame(frame)
        grid.grid(sticky=N+S+E+W, column=0, row=2, columnspan=2)
        Grid.rowconfigure(frame, 2, weight=1)
        Grid.columnconfigure(frame, 0, weight=1)

        #Definition der Schriften (Art, Groesse und Dicke)
        global helv36
        helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
        global helv22
        helv22 = tkFont.Font(family='Helvetica', size=22, weight='normal')

        #Initialisierung der Liste für die Buttons
        btnList = []
        
        #Konfigurieren der Buttons und Verknuepfung mit den entsprechenden Methodenaufrufen
        btnList.append(Button(frame, text="Blau", foreground = 'white', background='blue', font=helv36, command=self.callbackBlue))
        btnList.append(Button(frame, text="Rot", foreground = 'white', background='red', font=helv36, command=self.callbackRed))
        btnList.append(Button(frame, text="Lila", foreground = 'white', background='purple', font=helv36, command=self.callbackPurple))
        btnList.append(Button(frame, text="Gelb", foreground = 'black', background='yellow', font=helv36, command=self.callbackYellow))

        #Erzeugung des Labels
        #Label muss global erzeugt werden, damit es spaeter aktualisiert werden kann!
        global label
        #Erzeugung der Textvariablen für das Label, damit dieses spaeter aktualisiert werden kann.
        global StatusTextVar 
        self.StatusTextVar = StringVar()
        label = Label(frame, font=helv22, anchor=NW, textvariable=self.StatusTextVar, justify=LEFT, wraplength=700)
        label.grid(row=2, columnspan="2", sticky=N+S+E+W)
        self.StatusTextVar.set("Bitte wählen Sie das zu produzierende Produkt aus und legen Sie den Transponder auf das Lesegerät") 

        #Inititalisierung des Indexes
        index = 0
        #Erzeugung der Buttons im Grid-Layout
        for x in range(2):
            for y in range(2):
                btn = btnList[index]
                index = index +1
                btn.grid(column=x, row=y, sticky=N+S+E+W)

        #Skalierung der Buttons anhand der Fenstergroesse in X-Richtung
        for x in range(2):
            Grid.columnconfigure(frame, x, weight=1)

        #Skalierung der Buttons anhand der Fenstergroesse in Y-Richtung
        for y in range(2):
            Grid.rowconfigure(frame, y, weight=1)

    #Definition der "toogle" Methoden, welche das Umschalten zwischen Maximiert und der oben festgelegten Fenstergroesse ermöglicht.
    def toogle_geom(self, event):
        geom=self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    
    #Aufruf der entsprechenden Methode (blau) zum Initialen Beschreiben der Transponder
    #Attribut "after" wird verwendet, um eine Verzoegerung beim Labelupdate zu erzeugen (Angabe in Millisekunden)
    #Funktion "lamba" beschreibt das Label neu (hier mit dem entsprechenden Text)
    def callbackBlue(self):
        label.after(1000, lambda: self.StatusTextVar.set("Transponder wird beschrieben. Bitte warten ..."))
        label.after(3000, lambda: self.StatusTextVar.set("Transponder mit Metadaten für blaues Produkt beschrieben"))
        write_blue.init()
        label.after(3000, lambda: self.StatusTextVar.set("Bitte wählen Sie das nächste zu produzierende Produkt aus und legen Sie den Transponder auf das Lesegerät"))
        
    #Aufruf der entsprechenden Methode (rot) zum Initialen Beschreiben der Transponder
    def callbackRed(self):
        label.after(1000, lambda: self.StatusTextVar.set("Transponder wird beschrieben. Bitte warten ..."))
        label.after(3000, lambda: self.StatusTextVar.set("Transponder mit Metadaten für rotes Produkt beschrieben"))
        self.StatusTextVar.set("Transponder mit Metadaten für rotes Produkt beschrieben")
        write_red.init()
        label.after(3000, lambda: self.StatusTextVar.set("Bitte wählen Sie das nächste zu produzierende Produkt aus und legen Sie den Transponder auf das Lesegerät"))

    #Aufruf der entsprechenden Methode (lila) zum Initialen Beschreiben der Transponder
    def callbackPurple(self):
        label.after(1000, lambda: self.StatusTextVar.set("Transponder wird beschrieben. Bitte warten ..."))
        label.after(3000, lambda: self.StatusTextVar.set("Transponder mit Metadaten für lila Produkt beschrieben"))
        write_purple.init()
        label.after(3000, lambda: self.StatusTextVar.set("Bitte wählen Sie das nächste zu produzierende Produkt aus und legen Sie den Transponder auf das Lesegerät"))

    #Aufruf der entsprechenden Methode (gelb) zum Initialen Beschreiben der Transponder
    def callbackYellow(self):
        label.after(1000, lambda: self.StatusTextVar.set("Transponder wird beschrieben. Bitte warten ..."))
        label.after(3000, lambda: self.StatusTextVar.set("Transponder mit Metadaten für gelbes Produkt beschrieben"))
        write_yellow.init()
        label.after(3000, lambda: self.StatusTextVar.set("Bitte wählen Sie das nächste zu produzierende Produkt aus und legen Sie den Transponder auf das Lesegerät"))
        
        
#Erzeugung des Fensterobjekts    
root=Tk()
#Bennung des Fenstertitels
root.title("Produktauswahl")
#Uebergabe an Programmklasse
program = Program(root)

#Ausfuehren des Fensters in einer Schleife
root.mainloop()
