from ttkwidgets import CheckboxTreeview
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import os
from DbDataloader import *
class DataLoader():
    def __init__(self,master):
        self.anne={}
        self.master=Toplevel(master)
        master.wait_visibility(self.master)
        self.master.grab_set()
        self.master.minsize(900,680)
        self.master.resizable(width=False,height=True)
        self.tree = CheckboxTreeview(self.master,height=25)
        os.chdir("DonneJson")
        with open("DonneUtile.json","r") as rf:
            self.anne.update(json.load(rf))
        rf.close()
        os.chdir("..")
        self.Nomfichier=os.listdir("DonneJson")
        self.Nomfichier.sort(reverse=True)
        self.modeTransaction=False
        self.db=DbDataloader(self.modeTransaction,self.master)
        self.main()
    #Fonction pour lire les fichiers json deja dans le module DataAcquisition
    def main(self):
        choice= messagebox.askyesno("askquestion","Cliquer sur Oui pour charger les données en mode Trasactionnel")
        if choice :
            self.modeTransaction=True
            self.db.conn.start_transaction()
            self.master.title("Data Loader : Mode Transanction=­OUI")
            self.create_widgets()
        else:
            self.modeTransaction=False
            self.master.title("Data Loader : Mode Transanction=­NON")
            self.create_widgets("Non Transanction")
    def lireFichier(self):
        label_welcome1 = Label(self.master,text="Prévisualiser les données",
        borderwidth = 7,
        width = 40,
        relief="groove"
        )
        label_welcome1.grid(row = 1, column = 0, padx = 50)
        label_welcome2 = Label(self.master,text="Selectionner le fichier pour la lecture")
        label_welcome2.grid(row = 2, column = 0, )
        listbox = Listbox(self.master, width=40, height=20,selectmode=SINGLE)
        i=0
        for fichier in self.Nomfichier:
            if "2" in fichier:
                listbox.insert(i, fichier)
                i=i+1
        def afficherObjet(Obj):
            try:
                os.chdir("DonneJson")
                textFichier={}
                with open(Obj,"r") as rf:
                    textFichier.update(json.load(rf))
                rf.close() 
                if textFichier:
                    texte="{\n"
                    for key,val in  textFichier.items():
                        b ="\t{\n"
                        c="\t"+str(key)+" :\n"
                        d=""
                        for key1,val1 in val.items():
                            d=str(d)+"\t\t"+str(key1)+" :"+" "+str(val1)+"\n"
                        e="\t},\n"
                        texte=texte+b+c+d+e
                    texte=texte+"}\n"
                texte=texte+"\n\n\t"+str(len(textFichier))+" Objets eenregistrer dans le fichier "+Obj 
                os.chdir("..")
                return texte
            except Exception as e:
                print(e)
                messagebox.showerror(title="Erreur !!!", message="Fichier "+Obj+" introuvable")
        def selected_item():
            try:
                if  listbox.get(listbox.curselection()):
                    textes=afficherObjet(listbox.get(listbox.curselection()))
                    if textes:
                        fil = Toplevel(self.master)
                        # fenetre blocante : empeche l’ouverture de fenetres identiques
                        self.master.wait_visibility(fil)
                        fil.grab_set()
                        # end fenetre blocante
                        fil.geometry("600x600")
                        fil.title("Fichier :"+listbox.get(listbox.curselection()))
                        yscroll = Scrollbar(fil)
                        yscroll.pack(side=RIGHT, fill=Y)
                        xscroll = Scrollbar(fil, orient=HORIZONTAL)
                        xscroll.pack(side=BOTTOM, fill=X)
                        text1 = Text(fil,wrap=NONE,height=30, width=100,yscrollcommand=yscroll.set,
                        xscrollcommand=xscroll.set)  
                        text1.config(state="normal")
                        text1.insert("1.0",textes)   
                        text1.pack(side=LEFT) 
                        yscroll.config(command=text1.yview)   
                        xscroll.config(command=text1.xview)             
                        fil.mainloop()
                        fil.quit()
            except :
                messagebox.showerror(title="Erreur !!!", message="Vous selectionner un fichier d`abord")
        listbox.grid(row = 3, column = 0, pady =20 )
        btn = Button(self.master, text='Lire Le Fichier', command=selected_item)
        btn.grid(row = 3, column = 1, pady =6 )
    #Fonction pour cocher les dates ensuite enregistrer vers la bases de donneef
    def CaseCocher(self,mode="Transanction"): 
        style = Style() 
        style.configure('W.TButton', font =
               ('calibri', 15, 'bold', 'underline'),
                foreground = 'red')
        style.configure('G.TButton', font =
               ('calibri', 15, 'bold','underline'),
                foreground = 'green')
        #recuperer les ligne selectionnes 
        def getCheckDict(obj):
            selectDate={}
            for t in obj:
                try:
                    selectDate[t[:7]].append(t)
                except:
                    selectDate[t[:7]]=[]
                    selectDate[t[:7]].append(t)
            return  selectDate
        def valider():
            if self.tree.get_checked():
                #si il choisi oui (en transanction)
                choice= messagebox.askyesno("Askquestion!!!","Vous etes sur pour la validation")
                if choice==True:
                    self.db.Alldayselected =getCheckDict(self.tree.get_checked())
                    if self.modeTransaction == False:
                        #Mode Non Transactionnel
                        self.db.insertCommunique()
                    else:
                        #Mode Transaction
                        self.db.insertCommunique()       
            else:
                messagebox.showerror(title="Erreur !!!", message="Cocher une case au moins !!!")
        def commit():
            choice= messagebox.askyesno("Askquestion!!!","Vouliez-vouz faire un commit?")
            if choice==True:
                    messagebox.showinfo("Info","Mode Commit en cours")
                    self.db.conn.commit()
                    self.db.conn.start_transaction()
        def rollback():
            choice= messagebox.askyesno("Askquestion!!!","Vouliez-vouz faire un rollback?")
            if choice==True:
                    messagebox.showinfo("Info","Mode rollback en cours ")
                    self.db.conn.rollback()
                    self.db.conn.start_transaction()
        label_welcomec = Label(self.master,
        text="La liste des fichiers json obtenus avec leur arborescence",
        borderwidth = 7,
        relief="groove")
        label_welcomec.grid(row = 1, column = 3, pady = 8)
        vsb = Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        vsb.place(relx=0.978, rely=0.175, relheight=0.713, relwidth=0.020)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.insert("", "end", "ALL", text="SELECT ALL")
        for key,val in self.anne.items():
            self.tree.insert("ALL", "end", key, text=key)
            for i in val:
                self.tree.insert(key,"end", i, text=i)
        self.tree.grid(row = 3, column = 3, pady = 2)
        button_name=Button(self.master,text="Valider",command=valider)
        button_name.grid(row = 3, column = 4, pady = 2)
        if mode=="Transanction":
            commit_buttoon_name=Button(self.master,text="COMMIT",command=commit,style="G.TButton"
            )
            commit_buttoon_name.grid(row = 4, column = 3, pady = 2)
            rollback_buttoon_name=Button(self.master, text = 'ROLLBACK !',
            style = 'W.TButton',command=rollback)
            rollback_buttoon_name.grid(row = 4, column = 4, pady = 2)
    def create_widgets(self,mode="Transanction"):
        self.lireFichier()
        self.CaseCocher(mode)
    def mains(self,obj):
        obj.master.mainloop()
        obj.db.conn.rollback()
