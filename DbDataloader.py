from ttkwidgets import CheckboxTreeview
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import json
import os
import mysql.connector as db
class DbDataloader:
    def __init__(self,modeTransaction,master):
        self.conn=self.dbConnect()
        self.ville={}
        os.chdir("DonneCommune")
        with open("AllCommunes.json","r") as rf:
            self.ville.update(json.load(rf))
        rf.close()
        os.chdir("..")
        self.Alldayselected = {}
        #Variable pour les donnees 
        self.donneJsonselected={}
        self.donne={}
        self.modeTransaction=modeTransaction
    def getAllDonneSelected(self):
        self.donneJsonselected={}
        os.chdir("DonneJson")
        for keys,vals in self.Alldayselected.items():
            nomfichier=keys+".json"
            self.donne={}
            try:
                with open(nomfichier,"r") as rf:
                    self.donne.update(json.load(rf))
                rf.close()
            except:
                    pass
            for day in vals:
                self.donneJsonselected[day]=self.donne[day]
                if self.donneJsonselected[day]["localite"]:
                    self.localite={}
                    #self.donneJsonselected[day]["localite"]=self.gerCasDebut(self.donneJsonselected[day]["localite"],self.donneJsonselected[day]["nbrecommunautaire"])
                    for key,val in self.donneJsonselected[day]["localite"].items():
                        if key in self.ville:
                            if self.ville[key].upper() not in self.localite:
                                self.localite[self.ville[key].upper()]=0
                            self.localite[self.ville[key].upper()]=self.localite[self.ville[key].upper()]+val
                    self.donneJsonselected[day]["localite"]=self.localite
        os.chdir("..")
        return self.donneJsonselected
    #connected to database
    def dbConnect(self):
        try:
            conn= db.connect(host= "localhost",
                                        user="admin_CovidModeler",
                                        password="dic2tr",
                                        database="covidModeler")
            conn.autocommit= True
            return conn
        except db.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0],e.args[1]))
            sys.exit(1)
        
    #Enregistrement Des Donnees dans la base
    def insertCommunique(self):
        for key, val in self.getAllDonneSelected().items():
            curseur= self.conn.cursor()
            request= "SELECT * FROM communique WHERE date_communique= %s"
            date=(key,)
            curseur.execute(request, date)
            result=curseur.fetchall()
            if result:
                #communique existe(Ecraser ou Ignorer)
                choix= messagebox.askyesno("Askquestion", "Cliquer Oui pour Ecrasez Non Ignorez")
                if choix == True:
                    #Ecraser données
                    self.deleteCommunique(key)
                    self.insertInToCommunique(val, key)
                    self.insertInToCasLocalite(val["localite"], key)
                    
            else:
                #Enregistrez données dans la base
                self.insertInToCommunique(val, key)
                self.insertInToCasLocalite(val["localite"], key)

            curseur.close()

    #inserer cas par localite
    def insertInToCommunique(self, val, dateCommunique):
        curseur= self.conn.cursor()
        try:
            request= """INSERT INTO communique(nbre_test, nbre_nouveaux_cas, nbre_cas_contact, nbre_cas_communautaires,nbre_cas_importe,
                                                nbre_gueris, nbre_deces, nom_fichier_source, 
                                                date_heure_extraction, date_communique)
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            value=(val["nbretest"], val["nouveaucas"], val["nbrecontact"], val["nbrecommunautaire"], val["nbreimporte"], val["nbregueris"], val["nbredeces"], val["nomfichiersource"], val["date_heure_extraction"], dateCommunique)
            curseur.execute(request, value)
        except Exception as e:
            print(e)
            message="Date "+dateCommunique
            messagebox.showerror("Erreur d'insertion !!!", message)
                
        curseur.close()

    def insertInToCasLocalite(self, localite, dateCommunique):
        #self.conn.autocommit = autocommit
        curseur= self.conn.cursor()
        for key, val in localite.items():
            request= "SELECT commune_id, depart_id FROM commune WHERE nom_localite like %s"
            nom_localite=(key, )
            curseur.execute(request, nom_localite)
            result=curseur.fetchone()
            if result:
                commune_id= result[0]
                depart_id= result[1]
                try:
                    request= """INSERT INTO cas_localite(commune_id, depart_id, nbre_cas, date_communique)
                                                        VALUES(%s, %s, %s, %s)"""
                    value=(commune_id, depart_id, val, dateCommunique)
                    
                    curseur.execute(request, value)
                except Exception as e:
                    print(e)
                    messagebox.showerror(title="Erreur d'insertion !!!", message="Fichier "+dateCommunique+" localite "+nom_localite)
                
            else:
                request= "SELECT depart_id FROM departement WHERE nom_localite like %s"
                nom_localite=(key, )
                curseur.execute(request, nom_localite)
                result=curseur.fetchone()
                depart_id= result[0]
                try:
                    request= """INSERT INTO cas_localite(depart_id, nbre_cas, date_communique)
                                                        VALUES(%s, %s, %s)"""
                    value=(depart_id, val, dateCommunique)
                    curseur.execute(request, value)
                except:
                    print(e)
                    messagebox.showerror(title="Erreur d'insertion !!!", message="Fichier "+dateCommunique+" localite "+nom_localite)
                
                
        curseur.close()
    
    #Supprimer Communique
    def deleteCommunique(self, dateCommunique):
        curseur= self.conn.cursor()
        #Delete From table cas_localite
        request= """DELETE FROM cas_localite WHERE date_communique= %s"""
        date=(dateCommunique,)
        curseur.execute(request, date)

        #Delete from table communique
        request= """DELETE FROM communique WHERE date_communique= %s"""
        date=(dateCommunique,)
        curseur.execute(request, date)

        curseur.close()



