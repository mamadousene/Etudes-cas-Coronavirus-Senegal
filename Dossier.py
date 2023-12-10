from tkinter import messagebox
import os
import sys
from os import listdir
def getCheminLastImage():
    Nom_Dossier= "TweetAllImage"
    os.chdir(os.path.abspath("."))
    if not os.path.exists(Nom_Dossier):
        messagebox.showwarning("Attention","Veuiller telecharger les images d abord pas de dossier ")
        sys.exit(1)
    anne=listdir(Nom_Dossier)[-1:][0]
    os.chdir(Nom_Dossier)
    jour=listdir(anne)[-1:][0]
    os.chdir(anne)
    os.chdir(jour)
    tabLinkjour=[]
    tabDate={}
    date=anne+"-"+jour
    for tjour in listdir():
        chaineLink="./"+Nom_Dossier+"/"+anne+"/"+jour+"/"+tjour
        tabLinkjour.append(chaineLink)
    tabDate[date]=tabLinkjour
    os.chdir("..")
    os.chdir("..")
    os.chdir("..")
    return tabDate
def getCheminImage():
    tabLinkMois={}
    Nom_Dossier= "TweetAllImage"
    os.chdir(os.path.abspath("."))
    if not os.path.exists(Nom_Dossier):
        messagebox.showwarning("Attention","Veuiller telecharger les images d abord pas de dossier ")
        sys.exit(1)
    for par in listdir(Nom_Dossier):
        os.chdir(Nom_Dossier)
        tablAllLinkJour=[]
        for fil in listdir(par):
            os.chdir(par)
            tabLinkjour=[]
            os.chdir(fil)
            date=par+"-"+fil
            tabDate={}
            for filess in listdir():
                chaineLink="./"+Nom_Dossier+"/"+par+"/"+fil+"/"+filess
                tabLinkjour.append(chaineLink)
            tabDate[date]=tabLinkjour
            tablAllLinkJour.append(tabDate)
            os.chdir("..")
            os.chdir("..")
        os.chdir("..")
        tabLinkMois[par]=tablAllLinkJour
    return  tabLinkMois