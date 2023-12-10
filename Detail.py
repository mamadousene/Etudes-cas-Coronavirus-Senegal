from tkinter import *
from flottante import *
class Detail():
    #fenetre qui est crèè quand on fait une clique sur une règion
    def __init__(self,master,date, region):
        self.window = Toplevel(master)
        # fenetre blocante : empeche l’ouverture de fenetres identiques
        self.master=master
        master.wait_visibility(self.window)
        self.window.grab_set()
        self.window.title('Rèpartition de '+region)
        self.window.configure(bg="#95A5A6")
        self.date=date
        self.region=region
        self.lab1 =Label(self.window, text='Nombre de cas ', bg='#95A5A6',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.lab2 =Label(self.window, text='Nombre de cas communautaires', bg='#95A5A6',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.lab3 =Label(self.window, text='Nombre de cas contact ', bg='#95A5A6',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.frame0 = Frame(self.window, bg='#95A5A6')

         # creation des composants
        self.create_detail_button()
        # empaquetage
        self.lab1.grid(row=0,pady=10,padx=10,sticky=W)
        self.lab2.grid(row=1,padx=10,sticky=W)
        self.lab3.grid(row=2,pady=10,padx=10,sticky=W)
        self.frame0.grid(row=3)
    def create_detail_button(self):
        B1 = Button(self.frame0,text="Details", font=("Arial", 10),command=self.flottantp)
        B1.pack(side=RIGHT)


    def flottant(self,master,date,regio):
        pe=flottante(master,date,regio)
        region=nbrCasParRegion(date)
        dep = nbrCasParDepartement(regio,date)
        if (regio=="dakar"):
            pe.canvas2.itemconfigure(pe.lrufisque,text="{} cas".format(dep["rufisque"]))
            pe.canvas2.itemconfigure(pe.ldakar,text="{} cas".format(dep["dakar"]))
            pe.canvas2.itemconfigure(pe.lpikine,text="{} cas".format(dep["pikine"]))
            pe.canvas2.itemconfigure(pe.lguediewaye,text="{} cas".format(dep["guediawaye"]))
        
        if (regio=="diourbel"):
            pe.canvas2.itemconfigure(pe.ldiourbel,text="{} cas".format(dep["diourbel"]))
            pe.canvas2.itemconfigure(pe.lbambey,text="{} cas".format(dep["bambey"]))
            pe.canvas2.itemconfigure(pe.lmbacke,text="{} cas".format(dep["mbacke"]))

        if (regio=="fatick"):
            pe.canvas2.itemconfigure(pe.lfoundiougne,text="{} cas".format(dep["foundiougne"]))
            pe.canvas2.itemconfigure(pe.lfatick,text="{} cas".format(dep["fatick"]))
            pe.canvas2.itemconfigure(pe.lgossas,text="{} cas".format(dep["gossas"]))

        if (regio=="kaffrine"):
            pe.canvas2.itemconfigure(pe.lmalem,text="{} cas".format(dep["malem hodar"]))
            pe.canvas2.itemconfigure(pe.bourkilane,text="{} cas".format(dep["birkilane"]))
            pe.canvas2.itemconfigure(pe.lkaff,text="{} cas".format(dep["kaffrine"]))  

        if (regio=="louga"):
            pe.canvas2.itemconfigure(pe.llouga,text="{} cas".format(dep["louga"]))
            pe.canvas2.itemconfigure(pe.llinguere,text="{} cas".format(dep["linguere"]))
            pe.canvas2.itemconfigure(pe.lkebemer,text="{} cas".format(dep["kebemer"]))      

        if (regio=="kaolack"):
            pe.canvas2.itemconfigure(pe.lkaolack,text="{} cas".format(dep["kaolack"]))
            pe.canvas2.itemconfigure(pe.lnioro,text="{} cas".format(dep["nioro du rip"]))
            pe.canvas2.itemconfigure(pe.lguinguineo,text="{} cas".format(dep["guinguineo"]))      

        if (regio=="matam"):
            pe.canvas2.itemconfigure(pe.lmatam,text="{} cas".format(dep["matam"]))
            pe.canvas2.itemconfigure(pe.lranerou,text="{} cas".format(dep["ranerou ferlo"]))
            pe.canvas2.itemconfigure(pe.lkanel,text="{} cas".format(dep["kanel"]))      

        if (regio=="saint-louis"):
            pe.canvas2.itemconfigure(pe.ldagana,text="{} cas".format(dep["dagana"]))
            pe.canvas2.itemconfigure(pe.lpodor,text="{} cas".format(dep["podor"]))
            pe.canvas2.itemconfigure(pe.lndar,text="{} cas".format(dep["saint-louis"])) 

        if (regio=="sedhiou"):
            pe.canvas2.itemconfigure(pe.lbounkiling,text="{} cas".format(dep["boukiling"]))
            pe.canvas2.itemconfigure(pe.lgoudong,text="{} cas".format(dep["goudomp"]))
            pe.canvas2.itemconfigure(pe.lsedhiou,text="{} cas".format(dep["sedhiou"])) 

        if (regio=="tambacounda"):
            pe.canvas2.itemconfigure(pe.ltambacounda,text="{} cas".format(dep["tambacounda"]))
            pe.canvas2.itemconfigure(pe.lkoumpentoun,text="{} cas".format(dep["koumpentoum"]))
            pe.canvas2.itemconfigure(pe.lgoudiry,text="{} cas".format(dep["goudiry"])) 
            pe.canvas2.itemconfigure(pe.lbakel,text="{} cas".format(dep["bakel"])) 

        if (regio=="thies"):
            pe.canvas2.itemconfigure(pe.lthies,text="{} cas".format(dep["thies"]))
            pe.canvas2.itemconfigure(pe.lmbour,text="{} cas".format(dep["mbour"]))
            pe.canvas2.itemconfigure(pe.ltivaoune,text="{} cas".format(dep["tivaouane"]))

        if (regio=="ziguinchor"):
            pe.canvas2.itemconfigure(pe.lziguinchor,text="{} cas".format(dep["ziguinchor"]))
            pe.canvas2.itemconfigure(pe.lbignona,text="{} cas".format(dep["bignona"]))
            pe.canvas2.itemconfigure(pe.loussouye,text="{} cas".format(dep["oussouye"]))

        if (regio=="kolda"):
            pe.canvas2.itemconfigure(pe.lkolda,text="{} cas".format(dep["kolda"]))
            pe.canvas2.itemconfigure(pe.lvelingara,text="{} cas".format(dep["velingara"]))
            pe.canvas2.itemconfigure(pe.lmedinayoro,text="{} cas".format(dep["medina yoro foulah"]))

        if (regio=="kedougou"):
            pe.canvas2.itemconfigure(pe.lkedougou,text="{} cas".format(dep["kedougou"]))
            pe.canvas2.itemconfigure(pe.lsalemata,text="{} cas".format(dep["salemata"]))
            pe.canvas2.itemconfigure(pe.lsaraya,text="{} cas".format(dep["saraya"]))      

        
    





        pe.window.mainloop()
    
    def flottantp(self):
        self.flottant(self.master,self.date,self.region)

