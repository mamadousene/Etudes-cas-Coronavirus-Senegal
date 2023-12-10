from tkinter import messagebox
import ImageToText  as it
from datetime import datetime
class ExtractCom:
    def __init__(self,linkImage):
        self.texte=it.contenuText(linkImage)
        self.tabContenu = self.texte.split("\n")
        self.nbretest=0
        self.darte_heure_extraction=str(datetime.now())[:19]
        self.date_communique=""
        self.nbrecontact=0
        self.nbrecommunautaire=0
        self.nbregueris=0
        self.nbredeces=0
        self.nomfichiersource=",".join(linkImage)
        self.casLocalite={}
        self.lastcaslocalite=1;
        self.search=["hlm","cap","des","zac","est","sur","mer","ben","fos","sud","sow","cpi","aif","sie","las"]
    def entete(self,test,test2):
        try:
            for cont in self.tabContenu:
                if test  in cont:
                    if test=="décé":
                        if "Aucun" or "A ce jour" or "jour" in cont:
                            return []
                        return cont
                    else:
                        return cont
            for cont2 in self.tabContenu:
                if test2 in cont2:
                    if test=="décé":
                        if "cun" or "ce jour" or "jour" in cont2:
                            return []
                        return cont2
                    else:
                        return cont2
        except:
            return []
    def getNombreCas(self,search1,search2):
        try:
            for mot in self.entete(search1,search2).split(",") :
                for nombre in mot.split():
                    try:
                        a=int(nombre)
                        if a>0:
                            return a
                        else:
                            return 0
                    except:
                        pass
        except:
            return 0
    def is_valid(self,mot):
        if "(" in mot:
            return False
        else:
            if mot=="Cité-Impéts-" or mot =="entre" or mot=="dont" or mot=="communautaire":
                return False
            else:
                if len(mot)>3 or mot.lower() in self.search:
                    return True
        return False
    def getCasLocalite(self,chaineCas):
        nombre=""
        zero=False
        nozero=False
        i=-1
        limitCahine = len(chaineCas)
        for lettre in chaineCas:
            i=i+1
            try:
                int(lettre)
                if i == limitCahine-1:
                    assert lettre!=chaineCas[-1:]
                if nozero:
                    nombre=nombre+lettre
                    break
                if zero:
                    nombre=lettre
                    break;
                if lettre=="0":
                    zero=True
                else:   
                    if  i>4 :
                        assert chaineCas[i-1]!="-"
                        assert chaineCas[i-2]!="-"
                    nozero=True
                nombre=lettre
            except:
                if nombre:
                    break
        tsbaC=chaineCas.split(" ")
        tablocalite=[]
        chiffString=0
        ti=-1
        for mot in tsbaC:
            ti=ti+1
            try:
                validnumber=int(mot)
                if ti==len(tsbaC)-1:
                    chiffString=validnumber
                    assert mot!=chaineCas[-1:]
                else:
                    if ti>0 and len(tsbaC[ti-1])>4 and tsbaC[ti-1][-1:]=="-":
                        tablocalite.append(mot)
            except:
                if mot=="it":
                    tablocalite.append("Petit")
                else:
                    if mot=="Patick":
                        tablocalite.append("Fatick")
                    else:
                        if mot=="E":
                            tablocalite.append("E")
                        else:
                            if mot=="it-Mbao":
                                tablocalite.append("Petit-Mbao")
                            else:
                                if mot=="-Domaines":
                                    tablocalite.append("Cité-Impot-et-Domaines")
                                else:
                                    if self.is_valid(mot) or str(chiffString)==chaineCas[-1:]:
                                        tablocalite.append(mot)
        nomlocalite=" ".join(tablocalite)
        try:
            if nomlocalite!="":
                if int(nombre)==0:
                    self.casLocalite[nomlocalite]=1
                else:
                    self.casLocalite[nomlocalite]=int(nombre)
                self.lastcaslocalite=self.casLocalite[nomlocalite]
        except:
            if  nomlocalite!="" or "importé" not in nomlocalite or "provenant" not in nomlocalite:
                self.casLocalite[nomlocalite]=self.lastcaslocalite
    def getLocalite(self):
        limit1 = "mission"
        limit2 = "patient"
        totallocalite=[]
        localitetab=[]
        indiceCom=0
        indicePat=0
        t=0
        for contLo in self.tabContenu:
            if limit1 in contLo :
                indiceCom=t
            if  limit2 in contLo:
                indicePat=t
                break;
            t=t+1
        localitetab = " ".join(self.tabContenu[indiceCom+1:indicePat])
        tsene=""
        pointvirgule=";"
        for a in localitetab.split("."):
            tsene=tsene+" ".join(a.split(":")[-1:])+pointvirgule
        tabfiltre = tsene.strip()
        tabfiltre= tabfiltre.split(";")
        localfinal=[]
        for tf in tabfiltre:
            tf=tf.strip()
            if tf:
                localfinal.append(tf)
        for tfinal in tabfiltre:
            newtfinal=tfinal.replace("et",",")
            for  tfvirgule in newtfinal.split(","): 
                self.getCasLocalite(tfvirgule.strip())
    def getAttribut(self):
        self.nbretest=self.getNombreCas("test","test");
        self.nbrecontact=self.getNombreCas("contact","cas con")
        self.nbrecommunautaire=self.getNombreCas("mission","mission")
        self.nbregueris=self.getNombreCas("patient","patient")
        self.nbredeces=self.getNombreCas("décé","décé")
        if self.nbrecommunautaire and self.nbrecommunautaire!=0:
            self.getLocalite()
    def verify(self,a):
        if a==None:
            return 0
        return a
    def getCasDict(self):
        self.getAttribut()
        casdict={}
        casdict["nbretest"]=self.nbretest
        casdict["nbretest"]=self.verify(casdict["nbretest"])
        casdict["nbrecontact"]=self.nbrecontact
        casdict["nbrecontact"]=self.verify(casdict["nbrecontact"])
        casdict["nbrecommunautaire"]=self.nbrecommunautaire
        casdict["nbrecommunautaire"]=self.verify(casdict["nbrecommunautaire"])
        casdict["nouveaucas"]=casdict["nbrecontact"]+casdict["nbrecommunautaire"]
        casdict["nbregueris"]=self.nbregueris
        casdict["nbregueris"]=self.verify(casdict["nbregueris"])
        casdict["nbredeces"]=self.nbredeces
        casdict["nbredeces"]=self.verify(casdict["nbredeces"])
        casdict["datecommunique"]= self.date_communique
        casdict["date_heure_extraction"]=self.darte_heure_extraction
        casdict["nomfichiersource"]=self.nomfichiersource
        casdict["localite"]=self.casLocalite
        return casdict  
