import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from time import sleep
import threading
class ProgressBar():
    def __init__(self,master):
        self.master=master
    def time(self):
        sleep(1)
    def LoadingTweet(self):
        self.fil = tk.Toplevel(self.master)
        # fenetre blocante : empeche l’ouverture de fenetres identiques
        self.master.wait_visibility(self.fil)
        self.fil.grab_set()
        # end fenetre blocante
        self.fil.geometry("500x200")
        self.fil.resizable(width=False,height=False )
        self.fil.title("\nChargement des Communiques depuis Twitter")
        self.pb1 = Progressbar(self.fil,orient=tk.HORIZONTAL, length=300, mode='indeterminate')
        self.pb1.pack(expand=True)
        self.pb1.start()
        self.t = threading.Thread(target=self.time)
        self.t.start()
        self.t.join()
        # Simulate long running process
        self.label_welcome=tk.Label(self.fil,text="Recherche des Communiques vers twitter",font="Bahnschrift 15")
        self.label_welcome.pack()
    """
    self.label_welcome1["text"]=str( self.loading)+" Communique Chargees depuis twitter"
    def ExtractDonneDujour(self):
        reponse = messagebox.askquestion("Question?","Voulez-vous telecharger le communique du jour ?")
        if reponse=="yes":
            pass
    def ExtractDonneAllJour(self):
        reponse = messagebox.askquestion("Question?","Voulez-vous telecharger tout les communique du jour")
        if reponse=="yes":
            self.LoadingTweet()
    """