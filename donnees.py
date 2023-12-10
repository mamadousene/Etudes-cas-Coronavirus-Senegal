import mysql.connector as db
import sys
import csv
import json
import os
class csvDonne:
    def __init__(self,don,date):
        self.donne=self.getJson(don)
        self.date=date
    def getJson(self,donnjson):
        donne={}
        donne["dooneregion"]=[]
        for key,val in donnjson.items():
            oneregion={}
            oneregion["region"]=key
            oneregion["nbrecas"]=val
            donne["dooneregion"].append(oneregion)
        return donne
    def csvRegion(self):
        Nom_Dossier="Donnecsv"
        if not os.path.exists(Nom_Dossier):
            try:
                os.mkdir(Nom_Dossier)
            except:
                messagebox.showerror("Erreur","Impossible de creer le dossier")
        os.chdir(Nom_Dossier)
        Nom_region="Region"
        if not os.path.exists(Nom_region):
            try:
                os.mkdir(Nom_region)
            except:
                messagebox.showerror("Erreur","Impossible de creer le dossier")
        os.chdir(Nom_region)
        nomfichier=self.date+".csv"
        data_file = open(nomfichier, 'w')
        csv_writer = csv.writer(data_file)
        count = 0
        employee_data=  self.donne["dooneregion"]
        for emp in employee_data:
            if count == 0:
                header = emp.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(emp.values())
        data_file.close()
        os.chdir("..")
        os.chdir("..")
    def csvDepart(self):
        Nom_Dossier="Donnecsv"
        if not os.path.exists(Nom_Dossier):
            try:
                os.mkdir(Nom_Dossier)
            except:
                messagebox.showerror("Erreur","Impossible de creer le dossier")
        os.chdir(Nom_Dossier)
        Nom_region="Departement"
        if not os.path.exists(Nom_region):
            try:
                os.mkdir(Nom_region)
            except:
                messagebox.showerror("Erreur","Impossible de creer le dossier")
        os.chdir(Nom_region)
        nomfichier=self.date+".csv"
        data_file = open(nomfichier, 'w')
        csv_writer = csv.writer(data_file)
        count = 0
        employee_data=  self.donne["dooneregion"]
        for emp in employee_data:
            if count == 0:
                header = emp.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(emp.values())
        data_file.close()
        os.chdir("..")
        os.chdir("..")
def dbConnect():
    try:
        conn= db.connect(host= "localhost",
                        user="admin_CovidModeler",
                        password="dic2tr",
                        database="covidModeler")
                

    except db.errors.InterfaceError as e:
        print("Error %d: %s" % (e.args[0],e.args[1]))
        sys.exit(1)
    return conn

#Nombre des cas par Region avant une date
def nbrCasParRegion(date):
    conn=dbConnect()
    curseur=conn.cursor(dictionary=True)
    req= """SELECT R.nom_localite, nbrCas FROM (SELECT D.region_id, SUM(nbre_cas) AS nbrCas FROM 
            (SELECT depart_id, nbre_cas FROM cas_localite WHERE date_communique< %s)SR NATURAL JOIN departement D GROUP BY(D.region_id))SSR 
            RIGHT OUTER JOIN region R on R.region_id= SSR.region_id ORDER BY nbrCas DESC;"""

    value=(date, )
    curseur.execute(req, value)
    result= curseur.fetchall()
    dictRegion={}
    if result:
        for val in result:
            if val["nbrCas"] ==None:
                dictRegion[val["nom_localite"]]=0
            else:
                dictRegion[val["nom_localite"]]=int(val["nbrCas"])
    curseur.close()
    return dictRegion

#Somme des cas contact, communautaire... inferieure à une date
def totalCas(date):
    conn=dbConnect()
    req= """SELECT SUM(nbre_test) AS totalTest, SUM(nbre_nouveaux_cas) AS totalNouvCas, SUM(nbre_cas_contact) AS totalCasContact, 
                SUM(nbre_cas_communautaires) AS totalCommunautaire, SUM(nbre_gueris) AS totalGueris, SUM(nbre_deces) AS totalDeces 
                FROM communique WHERE date_communique< %s"""
    curseur=conn.cursor(dictionary=True)
    value=(date, )
    curseur.execute(req, value)
    result= curseur.fetchone()

    if result:
        for val in result:
            if result[val] ==None:
                result[val]=0
            else:
                result[val]=int(result[val])
    curseur.close()
    return result

#nbr des cas des departements d'une region avant une date
def nbrCasParDepartement(region, date):
    conn=dbConnect()
    req= """SELECT departement, nbrCas FROM 
                (SELECT depart_id, nom_localite AS departement FROM departement WHERE 
                    region_id=(SELECT region_id FROM region R WHERE R.nom_localite LIKE %s))SR 
                NATURAL JOIN (SELECT depart_id, SUM(nbre_cas) AS nbrCas FROM cas_localite WHERE date_communique< %s GROUP BY (depart_id))SSR;"""
    curseur=conn.cursor(dictionary=True)
    value=(region, date )
    curseur.execute(req, value)
    result= curseur.fetchall()

    casDepartement={}
    if result:
        for val in result:
            if val["nbrCas"]==None:
                casDepartement[val["departement"]]=0
            else:
                casDepartement[val["departement"]]=int(val["nbrCas"])
    #return dictRegion
    curseur.close()
    return casDepartement

#nombre cas d'une region par jour du debut à la date
def courbeParJour(date, region):
    conn=dbConnect()
    req= """SELECT date_communique, SUM(nbre_cas) AS nbrCas FROM (SELECT depart_id FROM departement WHERE 
                region_id=(SELECT region_id FROM region WHERE nom_localite like %s))SR NATURAL JOIN 
                (SELECT date_communique, depart_id, nbre_cas FROM cas_localite WHERE date_communique < %s)SSR 
                GROUP BY(date_communique) ORDER BY(date_communique);"""
    curseur=conn.cursor(dictionary=True)
    value=(region, date )
    curseur.execute(req, value)
    result= curseur.fetchall()

    dates=[]
    nbrCas=[]
    if result:
        for val in result:
            dates.append(str(val["date_communique"].isoformat()))
            if val["nbrCas"]==None:
                nbrCas.append(0)
            else:
                nbrCas.append(int(val["nbrCas"]))
    curseur.close()
    return (dates, nbrCas)

#nombre cas d'une region par jour du debut à la date
def courbeParMois(date, region):
    conn=dbConnect()
    
    req= """SELECT DATE_FORMAT(date_communique, '%m-%Y') AS mois, SUM(nbre_cas) AS nbrCas FROM 
                (SELECT depart_id FROM departement WHERE region_id=(SELECT region_id FROM region WHERE nom_localite like %s))SR 
                NATURAL JOIN (SELECT date_communique, depart_id, nbre_cas FROM cas_localite WHERE date_communique < %s)SSR 
                GROUP BY mois;"""
    curseur=conn.cursor(dictionary=True)
    value=(region, date )
    curseur.execute(req, value)
    result= curseur.fetchall()

    dates=[]
    nbrCas=[]
    if result:
        for val in result:
            dates.append(val["mois"])
            if val["nbrCas"]==None:
                nbrCas.append(0)
            else:
                nbrCas.append(int(val["nbrCas"]))
    curseur.close()
    return (dates, nbrCas)
