import Dossier as ds
import json
import os
from  ExtractCom  import *
import shutil
import linkimage as lki
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import *
from time import sleep
import threading 
from ProgressBar import *
class ExtracInfoUtile:
    def __init__(self,master):
        self.master=master
        self.TabLinkImage={}
        self.Nom_Dossier="DonneJson"
        self.donne={}
        self.LastTabLinkImage={}
        self.ville={}
        self.pgpg=ProgressBar(self.master)
    def getDonneJour(self,linkimage):
        es =ExtractCom(linkimage)
        return es.getCasDict()
    def getJsonTextFichierDuJour(self,progress):
        if lki.fonctionMain(progress,"First"):
            messagebox.showinfo("Info","Fin de Telechargement des Images")
            progress.pb1.stop()
            progress.fil.title("Extraction des Donnees depuis les Images vers des Fichier JSON")
            messagebox.showinfo("Info","Debut Extraction des Donnees depuis les Images vers des Fichier JSON")
            progress.pb1["value"]=0
            progress.label_welcome.config(text="")
            progress.fil.update_idletasks()
            self.LastTabLinkImage=ds.getCheminLastImage()
            self.ville={}
            os.chdir(os.path.abspath("."))
            if not os.path.exists(self.Nom_Dossier):
                try:
                    os.mkdir(self.Nom_Dossier)
                except:
                    messagebox.showerror("Erreur","Impossible de creer le dossier")
            os.chdir(self.Nom_Dossier)
            for keys,vals in self.LastTabLinkImage.items():
                nomfichier=keys[:7]+".json"
                if not os.path.exists(nomfichier):
                    try:
                        fichier =open(nomfichier,"x")
                        fichier.close()
                    except Exception as e:
                        messagebox.showerror("Erreur","Impossible de creer le fichier")
                if not os.path.exists("DonneUtile.json"):
                    try:
                        fichier =open("DonneUtile.json","x")
                        fichier.close()
                    except Exception as e:
                        messagebox.showerror("Erreur","Impossible de creer le fichier")
                else:
                    try:
                        with open("DonneUtile.json","r") as rf:
                            self.ville.update(json.load(rf))
                        rf.close()
                    except:
                        pass
                try:
                    self.donne={}
                    try:
                        with open(nomfichier,"r") as rf:
                            self.donne.update(json.load(rf))
                        rf.close()
                    except:
                        pass
                    if keys not in self.donne:
                        pourcentage = 100
                        progress.pb1["value"]=pourcentage
                        texte="Jour :"+keys+"Mois =>"+keys[:7]
                        tf="100%\n\n"+texte
                        progress.label_welcome.config(text=tf)
                        progress.fil.update_idletasks()
                        os.chdir("..")
                        self.donne[keys]=self.getDonneJour(vals)
                        self.donne[keys]["datecommunique"]=keys
                        try:
                            self.ville[keys[:7]].append(keys)
                        except:
                            self.ville[keys[:7]]=[]
                            self.ville[keys[:7]].append(keys)
                        os.chdir(self.Nom_Dossier)
                        with open(nomfichier,"w") as wf:
                            json.dump(self.donne,wf)
                            messagebox.showinfo("Réussi","donne bien enregistres dans le fichier")
                            wf.close()
                        with open("DonneUtile.json","w") as wf:
                            json.dump(self.ville,wf)
                            wf.close()
                        os.chdir("..")
                    else:
                        messagebox.showwarning("Attention","cet communique a ete deja extraire")
                except:
                    os.chdir("..") 
        else:
            messagebox.showwarning("Attention","le communique a ete deja telecharge merci")
            #bar1=app.bar()    
        self.pgpg.fil.destroy()
    def getJsonTextAllFichier(self,progress):
        if lki.fonctionMain(progress):
            messagebox.showinfo("Info","Fin de Telechargement des Images")
            progress.pb1.stop()
            progress.fil.title("Extraction des Donnees depuis les Images vers des Fichier JSON")
            messagebox.showinfo("Info","Debut Extraction des Donnees depuis les Images vers des Fichier JSON")
            progress.pb1["value"]=0
            progress.label_welcome.config(text="")
            progress.fil.update_idletasks()
            self.ville={}
            self.TabLinkImage=ds.getCheminImage()
            taille=len(self.TabLinkImage)
            self.donne={}
            os.chdir(os.path.abspath("."))
            if not os.path.exists(self.Nom_Dossier):
                try:
                    os.mkdir(self.Nom_Dossier)
                except:
                    messagebox.showerror("Erreur","Impossible de creer le dossier")
            else:
                try:
                    shutil.rmtree("DonneJson")
                    os.mkdir(self.Nom_Dossier)
                except:
                    messagebox.showerror("Erreur","Impossible de creer le dossier")
            try:
                os.chdir(self.Nom_Dossier)
                fichier =open("DonneUtile.json","x")
                fichier.close()
                os.chdir("..")
            except Exception as e:
                messagebox.showerror("Erreur","Impossible de creer le dossier") 
            posmois=0
            for keys,value in self.TabLinkImage.items():
                posmois=posmois+1
                os.chdir(self.Nom_Dossier)
                nomfichier=keys+".json"
                self.ville[keys]=[]
                if not os.path.exists(nomfichier):
                    try:
                        fichier =open(nomfichier,"x")
                        fichier.close()
                    except Exception as e:
                        messagebox.showerror("Erreur","Impossible de creer le dossier")    
                try:
                    os.chdir("..")
                    self.donne={}
                    taille1=len(value)
                    pos=1
                    textMois="Mois :"+keys+" => Extraction en cours­("+str(posmois)+"/"+str(taille)+")\n\n"
                    for link in value:
                        pourcentage = int(pos*100/taille1)
                        progress.pb1["value"]=pourcentage
                        tpou=str(pourcentage)+"%\n\n"
                        texte=str(pos)+"/"+str(taille1)+" Communiques extraires pour le mois =>"+keys
                        tf=tpou+textMois+texte
                        progress.label_welcome.config(text=tf)
                        progress.fil.update_idletasks()
                        for tjour,valjour in link.items():
                            self.donne[tjour]=self.getDonneJour(valjour)
                            self.donne[tjour]["datecommunique"]=tjour
                            self.ville[keys].append(tjour)
                        pos=pos+1
                    os.chdir(self.Nom_Dossier)
                    with open(nomfichier,"w") as wf:
                        json.dump(self.donne,wf)
                        wf.close()
                except Exception as e:
                    messagebox.showerror(e)
                os.chdir("..")
            os.chdir(self.Nom_Dossier)
            with open("DonneUtile.json","w") as wf:
                json.dump(self.ville,wf)
                wf.close()
            os.chdir("..")
        self.pgpg.fil.destroy()
    def CallAll(self):
        self.pgpg.LoadingTweet()
        t = threading.Thread(target=self.getJsonTextAllFichier,args=(self.pgpg,))
        self.pgpg.fil.after(1000,t.start())
        self.pgpg.fil.mainloop()
        self.pgpg.fil.quit()
    def CallOne(self):
        self.pgpg=ProgressBar(self.master)
        self.pgpg.LoadingTweet()
        t = threading.Thread(target=self.getJsonTextFichierDuJour,args=(self.pgpg,))
        self.pgpg.fil.after(1000,t.start())
        self.pgpg.fil.mainloop()
        self.pgpg.fil.quit()
if __name__ == '__main__':
    root = tk.Tk()
    es=ExtracInfoUtile(root)
    a=tk.Button(text="Dujour",command=es.CallAll)
    a.pack()
    root.mainloop()
    root.quit()
    
     