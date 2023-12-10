from ExtracInfoUtile import *
import Dossier as ds
import json
import os
from  ExtractCom  import *
import shutil
import linkimage as lki
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
class secondPage:
    def __init__(self,master):
        self.window = Toplevel(master)
    # fenetre blocante : empeche l’ouverture de fenetres identiques
        master.wait_visibility(self.window)
        self.window.grab_set()
        self.window.title("DataAcquisition")
        self.window.geometry("480x240")
        self.window.resizable(0,0)
        #self.window.iconbitmap("logo.ico")
        self.window.configure(bg="LightSeaGreen")
        # initialization des composants
        self.frame0=Frame(self.window,bg='LightSeaGreen')
        self.frame1=Frame(self.window,bg='LightSeaGreen')
        self.frame2=Frame(self.window,bg='LightSeaGreen')
        # creation des composants
        self.create_widgets()
        # empaquetage
        self.frame0.pack(pady=15)
        self.frame1.pack()
        self.frame2.pack(side=BOTTOM,fill=X)
        
    def exj(self):
        self.es=ExtracInfoUtile(self.window)
        self.es.CallOne()
        #self.bar()

        
    def exa(self):
        self.es=ExtracInfoUtile(self.window)
        self.es.CallAll()

    def create_widgets(self):
        self.create_title()
        self.create_jour_button()
        self.create_all_button()
        self.exit_button()

    
    def create_title(self):
        label1=Label(self.frame0,text="Bienvenu dans le module DataAcquisition",font=("Arial Bold", 15), bg='LightSeaGreen')
        label1.pack()

    def create_jour_button(self):
        B1 = Button(self.frame1,text="Telecharger et extraire le communique du jour", font=("Arial", 10),command=self.exj)
        B1.pack()
    def create_all_button(self):
        B2 = Button(self.frame1,text="Telecharger et extraire tous les fichiers", font=("Arial", 10),command=self.exa)
        B2.pack(pady=10)
        
 
        
    def exit_button(self):
        B2 = Button(self.frame2, text="Quitter", font=("Arial", 10), command=self.window.quit)
        B2.pack(side=RIGHT)

def dataAcquisition(master):
    app = secondPage(master)
    app.window.mainloop()

    