from Detail import *
from donnees import *
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk,ImageGrab  # pip install pillow
import os
class thirdpage(Frame):
    def __init__(self,master):
        self.window = Toplevel(master)
        self.master=master
    # fenetre blocante : empeche l’ouverture de fenetres identiques
        master.wait_visibility(self.window)
        self.window.grab_set()
        #self.window.geometry("820x620")
        #self.window.resizable(0,0)
        self.window.configure(bg="#95A5A6")
        self.window.title("DataExplorer")
        self.ta_variable = 90

        #Initialisation des compoosants
        #self.frame0 = Frame(self.window, bg='#95A5A6')
        self.btemp =Label(self.window, text='Choisir une date', bg='#95A5A6',fg="white", font=("Arial", 15))
        
        #Création des composants
        self.create_widgets()
        
        #empaquetage
        self.btemp.grid(row=0,pady=10)
        #self.frame0.pack(side=TOP,fill=X)
        
    def create_widgets(self):
        self.create_barre_temporelle()
        self.create_canvas()
        self.create_gencarte_button()
        self.create_telcarte_button()
        self.create_teldonnee_button()
        self.create_exit_button()
        
    def afficherTout(self,event=None):
        self.lab.configure(text = 'Vous avez choisi les dates du dèbut au :{0} / {1} / {2}'.\
                format(self.jour, self.mois, self.année))
    
    def test(self,event):
            """Fonction mise a jour carte nationale"""
            date= str(self.année)+'-'+str(self.mois)+'-'+str(self.jour)
            region=nbrCasParRegion(date)
            stat=totalCas(date) 
            self.canvas.itemconfigure(self.ldakar,text="{} cas".format(region["dakar"]))
            self.canvas.itemconfigure(self.ldiourbel,text="{} cas".format(region["diourbel"]))
            self.canvas.itemconfigure(self.lndar,text="{} cas".format(region["saint-louis"]))
            self.canvas.itemconfigure(self.llouga,text="{} cas".format(region["louga"]))
            self.canvas.itemconfigure(self.lmatam,text="{} cas".format(region["matam"]))
            self.canvas.itemconfigure(self.lkolda,text="{} cas".format(region["kolda"]))
            self.canvas.itemconfigure(self.lkaolak,text="{} cas".format(region["kaolack"]))
            self.canvas.itemconfigure(self.ltamba,text="{} cas".format(region["tambacounda"]))
            self.canvas.itemconfigure(self.lkaff,text="{} cas".format(region["kaffrine"]))
            self.canvas.itemconfigure(self.lthies,text="{} cas".format(region["thies"]))
            self.canvas.itemconfigure(self.lzig,text="{} cas".format(region["ziguinchor"]))
            self.canvas.itemconfigure(self.lsed,text="{} cas".format(region["sedhiou"]))
            self.canvas.itemconfigure(self.lkedougou,text="{} cas".format(region["kedougou"]))
            self.canvas.itemconfigure(self.lfatik,text="{} cas".format(region["fatick"]))
            self.canvas.itemconfigure(self.nat,text="A ce jour, le Sènègal compte: \n +{} tests\n +{} nouveaux cas\n +{} cas contact\n +{} cas communautaires\n +{} guèris\n +{} dècès".format(stat["totalTest"],stat["totalNouvCas"],stat["totalCasContact"],stat["totalCommunautaire"],stat["totalGueris"],stat["totalDeces"]))

    def save(self):
        x=Canvas.winfo_rootx(self.canvas)
        y=Canvas.winfo_rooty(self.canvas)
        w=Canvas.winfo_width(self.canvas)
        h=Canvas.winfo_height(self.canvas)
        ImageGrab.grab((x+30,y+50,1400,700)).save("cbas.png")


    def create_barre_temporelle(self):

        self.fra = Frame(self.window)
        self.jour, self.mois, self.année = 7, 3, 2020
        Scale(self.fra, length=150, orient=HORIZONTAL, sliderlength =25,label ='Jour :', from_=1., to=31, tickinterval =10,showvalue =0, command = self.setjouruency).pack(side=LEFT)
        Scale(self.fra, length=150, orient=HORIZONTAL, sliderlength =15,label ='Mois :', from_=1, to=12, tickinterval =3,showvalue =0, command = self.setmois).pack(side=LEFT)
        Scale(self.fra, length=150, orient=HORIZONTAL, sliderlength =25,label ='année :', from_=2020, to=2030, tickinterval =10,showvalue =0, command = self.setannée).pack(side=LEFT)

        self.fra.grid(row=1,column=0,columnspan=2,padx=20)
        self.lab = Label(self.window, text ='Vous avez choisi les dates du dèbut au 07/03/2020')
        self.lab.grid(row=1,column=2,columnspan=2,padx=10)
        self.window.bind('<Control-Z>', self.afficherTout)

    def setCurve(self):
        self.event_generate('<Control-Z>')
    def setjouruency(self,f):
        self.jour = f
        self.event_generate('<Control-Z>')
    def setmois(self, p):
        self.mois = p
        self.event_generate('<Control-Z>')
    def setannée(self, a):
        self.année = a
        self.event_generate('<Control-Z>')

    def Detaille(self,master,date,regio):
        master=self.master
        d=Detail(master,date,regio)
        region=nbrCasParRegion(date)
        d.lab1.configure(text='Nombre de cas : Inconnu')
        d.lab2.configure(text='Nombre de cas communautaires : '+str(region[regio]))
        d.lab1.configure(text='Nombre de cas contact : Inconnu')
        d.window.mainloop()

    def cas(self,event):
        date1= str(self.année)+'-'+str(self.mois)+'-'+str(self.jour)
        region=nbrCasParRegion(date1)
        if (event.x>=15 and event.x<35 and event.y>= 140 and event.y<=161 ):
            regio='dakar'
            self.Detaille(self.master, date1, regio)
        if (event.x>=380 and event.x<400 and event.y>= 280 and event.y<=300 ):
            regio='tambacounda'
            self.Detaille(self.master, date1, regio)
        if (event.x>=185 and event.x<205 and event.y>= 40 and event.y<=61 ):
            regio='saint-louis'
            self.Detaille(self.master, date1, regio)
        if (event.x>=140 and event.x<160 and event.y>= 110 and event.y<=130 ):
            regio='louga'
            self.Detaille(self.master, date1, regio)
        if (event.x>=340 and event.x<360 and event.y>= 110 and event.y<=140 ):
            regio='matam'
            self.Detaille(self.master, date1, regio)
        if (event.x>=230 and event.x<250 and event.y>= 220 and event.y<=240 ):
            regio='kaffrine'
            self.Detaille(self.master, date1, regio)
        if (event.x>=110 and event.x<130 and event.y>= 220 and event.y<=240 ):
            regio='fatick'
            self.Detaille(self.master, date1, regio)
        if (event.x>=110 and event.x<130 and event.y>= 190 and event.y<=210 ):
            regio='diourbel'
            self.Detaille(self.master, date1, regio)
        if (event.x>=160 and event.x<180 and event.y>= 240 and event.y<=261 ):
            regio='kaolack'
            self.Detaille(self.master, date1, regio)
        if (event.x>=75 and event.x<95 and event.y>= 140 and event.y<=160 ):
            regio='thies'
            self.Detaille(self.master, date1, regio)
        if (event.x>=110 and event.x<130 and event.y>= 345 and event.y<=355 ):
            regio='ziguinchor'
            self.Detaille(self.master, date1, regio)
        if (event.x>=180 and event.x<200 and event.y>= 340 and event.y<=360 ):
            regio='sedhiou'
            self.Detaille(self.master, date1, regio)
        if (event.x>=510 and event.x<530 and event.y>= 320 and event.y<=340 ):
            regio='kedougou'
            self.Detaille(self.master, date1, regio)
        if (event.x>=285 and event.x<305 and event.y>= 320 and event.y<=340 ):
            regio='kolda'
            self.Detaille(self.master, date1, regio)
        #root.mainloop()
    def create_canvas(self):
        
        self.image = Image.open("Regions_du_Senegal.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas=Canvas(self.window,width=1080,height=450)
        self.canvas.create_image(0,0,anchor=NW,image=self.photo)
        #--------------------------------- A ReECRIRE---------------------------------------
        self.nat=self.canvas.create_text(800,90,font=('Courrier',15),text=" A ce jour, les statistiques nationaux sont nulles")
        
        sdakar= self.canvas.create_bitmap(20,150,bitmap="questhead",foreground="red")
        self.ldakar = self.canvas.create_text(30, 170,text="0 cas")
        
        sndar= self.canvas.create_bitmap(195,50,bitmap="questhead",foreground="red")
        self.lndar = self.canvas.create_text(195,70, text="0 cas")
        
        slouga= self.canvas.create_bitmap(150,120,bitmap="questhead",foreground="red")
        self.llouga = self.canvas.create_text(150,140, text="0 cas")

        smatam= self.canvas.create_bitmap(350,120,bitmap="questhead",foreground="red")
        self.lmatam = self.canvas.create_text(350,140, text="0 cas")

        stamba= self.canvas.create_bitmap(390,290,bitmap="questhead",foreground="red")
        self.ltamba = self.canvas.create_text(390,310, text="0 cas")

        skaff= self.canvas.create_bitmap(240,230,bitmap="questhead",foreground="red")
        self.lkaff = self.canvas.create_text(240,270, text="0 cas")

        sfatik= self.canvas.create_bitmap(120,230,bitmap="questhead",foreground="red")
        self.lfatik = self.canvas.create_text(120,270, text=" cas")

        skaolak= self.canvas.create_bitmap(170,250,bitmap="questhead",foreground="red")
        self.lkaolak = self.canvas.create_text(170,270, text="0 cas")

        sdiourbel= self.canvas.create_bitmap(120,200,bitmap="questhead",foreground="red")
        self.ldiourbel = self.canvas.create_text(175,205, text="0 cas")

        sthies= self.canvas.create_bitmap(85,150,bitmap="questhead",foreground="red")
        self.lthies = self.canvas.create_text(85, 170, text="0 cas")

        skolda= self.canvas.create_bitmap(295,330,bitmap="questhead",foreground="red")
        self.lkolda = self.canvas.create_text(295,370, text="0 cas")

        szig= self.canvas.create_bitmap(120,355,bitmap="questhead",foreground="red")
        self.lzig = self.canvas.create_text(120,385, text="0 cas")

        ssed= self.canvas.create_bitmap(190,350,bitmap="questhead",foreground="red")
        self.lsed = self.canvas.create_text(190,375, text="0 cas")

        skedougou= self.canvas.create_bitmap(520,330,bitmap="questhead",foreground="red")
        self.lkedougou = self.canvas.create_text(520,390, text="0 cas")
        #--------------------------------- ---------------------------------------
      
        





        self.canvas.bind("<Button-1>",self.cas)
        #self.canvas.bind("<Button-1>",test)
        self.canvas.grid(row=2,columnspan=4,pady=30,padx=100)  


    def create_gencarte_button(self):
        gc = Button(self.window, text="Carte d'évolution journaliere", font=("Courrier", 10), bg='white', fg='#95A5A6')
        gc.bind("<Button-1>",self.test)
        gc.grid(row=3,column=0)
        
    def create_telcarte_button(self):
        telca = Button(self.window, text="Télécharger carte sous image.png", font=("Courrier", 10), bg='white', fg='#95A5A6',command=self.save)
        telca.grid(row=3,column=1)
        
    def create_teldonnee_button(self):
        teldon = Button(self.window, text="Télécharger Données sous csv", font=("Courrier", 10), bg='white', fg='#95A5A6',command=self.don)
        teldon.grid(row=3,column=2)
        
    def create_exit_button(self):
        dex = Button(self.window, text="Quitter", font=("Courrier", 10), bg='white', fg='#95A5A6',command=self.window.quit)
        dex.grid(row=3,column=3)

    def don(self):
        date=str(self.année)+'-'+str(self.mois)+'-'+str(self.jour)
        a=nbrCasParRegion(date)
        t=csvDonne(a,date)
        t.csvRegion()
        messagebox.showinfo("Resultat", "Données bien enregistrées")

def dataexplore(master):
    app = thirdpage(master)
    app.window.mainloop()

