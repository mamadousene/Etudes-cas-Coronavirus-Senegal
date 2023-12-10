"""DbEA.py
    MamadouLAMINESENE
    ML
"""
import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import os
from DbEA import *
class EvolutionAnalyser():
    """
        Iniatilisation de  la classee
    """
    def __init__(self,master):
        self.master=Toplevel(master)
        master.wait_visibility(self.master)
        self.master.grab_set()
        self.master.minsize(500,300)
        self.master.resizable(width=True,height=True)
        self.db=DbEA()
        self.ville=self.db.getDict()
        self.create_widgets()
        print(self.ville)
    """
        Creation des widgets()
    """
    def create_widgets(self):
        self.master.title("EvolutionAnalyser")
        self.SelectItems()
    """
        Foncion pour afficher les regions et les departements
    """
    def SelectItems(self):
        """
            elle retourne les departements
            concernant la region selectionnee
        """
        def getDepartement(regionSelected):
            self.comboDepart["values"]=self.ville[regionSelected]
            self.comboDepart.current(0)
        """
        Fonction pour gerer les evenements au niveau du select
        """
        def selectEvent(event):
            getDepartement(self.comboRegion.get())
            self.master.update_idletasks()
        """
            function pour la validation apres un departement selection
        """
        def valider():
            messagebox.showinfo("info",self.comboDepart.get())
        """
            function pour le lister toutes les regions du senegal
        """
        def region():
            self.labelTop = Label(self.master,
                text = "\nSelectionner un REGION",font="Bahnschrift 15")
            self.labelTop.grid(column=1, row=1,padx=4)
            region=[]
            for key,val in self.ville.items():
                region.append(key)
            self.comboRegion = Combobox(self.master, 
                                        values=region,state='readonly'
            )
            self.comboRegion.grid(column=1, row=2,padx=4)
            self.comboRegion.current(0)
            self.comboRegion.bind('<<ComboboxSelected>>',selectEvent)
        """
            function pour les departements du  region selectionne
        """
        def departement():
            self.labelTopD = Label(self.master,
                    text = "\nSelectionner un Departement",font="Bahnschrift 15")
            self.labelTopD.grid(column=2, row=1,padx=4)
            self.comboDepart = Combobox(self.master, 
                                        values=[],state='readonly'
            )
            self.comboDepart.grid(column=2, row=2,padx=4)
            getDepartement(self.comboRegion.get())
        """
         FUNCTION POUR APPELER LA FONCTION REGION() ET
         LA FONCTION DEPARTEMENT BUTTON
        """
        def button():
            region()
            departement()
            style = Style() 
            style.configure('G.TButton', font =
               ('calibri', 15, 'bold','underline'),
                foreground = 'green')
            Bvalider=Button(self.master,text="VALIDER",command=valider,style="G.TButton"
            )
            Bvalider.grid(column=4, row=2)
        button()

def data(master):
    app = EvolutionAnalyser(master)
    app.master.mainloop()