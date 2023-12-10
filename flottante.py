from tkinter import *
from donnees import *
from PIL import Image,ImageTk,ImageGrab
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
class flottante:
#fenetre qui est crèè quand on fait une clique sur une règion
    def __init__(self,master,date,region):
        self.window = Toplevel(master)
        # fenetre blocante : empeche l’ouverture de fenetres identiques
        master.wait_visibility(self.window)
        self.window.grab_set()
        self.date=date
        self.region=region
        self.window.title('Graphe d\' èvolution de '+region)
        self.window.configure(bg="#95A5A6")

        
        self.lab1 =LabelFrame(self.window, text='Courbe d\' èvolution des cas ', bg='#95A5A6',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.lab2 =LabelFrame(self.window, text='Carte des dèpartements', bg='#95A5A6',fg="white", font=("Arial", 15),bd=2,relief=SUNKEN)
        self.frame0 = Frame(self.window, bg='#95A5A6')

        #Création des composants
        self.create_widgets()
        
        #empaquetage
        self.lab1.grid(row=0,column=0,pady=10,padx=20)
        #self.lab2.grid(row=0,column=1,pady=10,padx=20)
        self.frame0.grid(row=1,columnspan=2,pady=10,padx=20)
    
    def create_widgets(self):
        self.create_canvas1()
        self.create_canvas2()
        self.create_telcarte_button()
        self.create_teldonnee_button()
        
    def create_canvas1(self):

        fig = Figure(figsize=(6,4),dpi=100)
        ax = fig.add_subplot(111)
        u,v=courbeParMois(self.date, self.region)      
        ax.plot(u,v)
        graph=FigureCanvasTkAgg(fig,self.window)
        self.canvas1=graph.get_tk_widget()
        self.canvas1.grid(row=0,column=1,pady=10,padx=20)

    def create_canvas2(self):
        self.canvas2=Canvas(self.lab1)
        l= self.region+'.png'
        self.image = Image.open(l)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas2.create_image(0,0,anchor=NW,image=self.photo)  
        if (self.region=='dakar'):
            self.lrufisque = self.canvas2.create_text(155,70, text="0 cas")
            self.lpikine = self.canvas2.create_text(105,115, text="0 cas")
            self.lguediewaye = self.canvas2.create_text(35,80, text="0 cas")
            self.ldakar = self.canvas2.create_text(55,130, text="0 cas")

        if (self.region=='thies'):
            self.lmbour = self.canvas2.create_text(165,70, text="0 cas")
            self.lthies = self.canvas2.create_text(125,115, text="0 cas")
            self.ltivaoune = self.canvas2.create_text(60,145, text="0 cas")
 
        if (self.region=='saint-louis'):
            self.lpodor = self.canvas2.create_text(155,80, text="0 cas")
            self.lndar = self.canvas2.create_text(85,140, text="0 cas")
            self.ldagana = self.canvas2.create_text(35,80, text="0 cas")

        if (self.region=='louga'):
            self.llinguere = self.canvas2.create_text(155,70, text="0 cas")
            self.llouga = self.canvas2.create_text(90,65, text="0 cas")
            self.lkebemer = self.canvas2.create_text(35,80, text="0 cas")

        if (self.region=='diourbel'):
            self.lmbacke = self.canvas2.create_text(155,80, text="0 cas")
            self.ldiourbel = self.canvas2.create_text(100,100, text="0 cas")
            self.lbambey = self.canvas2.create_text(50,80, text="0 cas")

        if (self.region=='fatick'):
            self.lgossas = self.canvas2.create_text(115,80, text="0 cas")
            self.lfoundiougne = self.canvas2.create_text(70,100, text="0 cas")
            self.lfatick = self.canvas2.create_text(50,80, text="0 cas")
        
        if (self.region=='ziguinchor'):
            self.lziguinchor = self.canvas2.create_text(155,130, text="0 cas")
            self.lbignona = self.canvas2.create_text(100,100, text="0 cas")
            self.loussouye = self.canvas2.create_text(50,135, text="0 cas")
        
        if (self.region=='sedhiou'):
            self.lgoudong = self.canvas2.create_text(155,130, text="0 cas")
            self.lsedhiou = self.canvas2.create_text(100,100, text="0 cas")
            self.lbounkiling = self.canvas2.create_text(50,85, text="0 cas")

        if (self.region=='kaffrine'):
            self.lkaff = self.canvas2.create_text(185,130, text="0 cas")
            self.lmalem = self.canvas2.create_text(140,100, text="0 cas")
            self.lbourkilane = self.canvas2.create_text(50,85, text="0 cas")

        if (self.region=='matam'):
            self.lkanel = self.canvas2.create_text(165,130, text="0 cas")
            self.lmatam = self.canvas2.create_text(110,100, text="0 cas")
            self.lranerou = self.canvas2.create_text(50,60, text="0 cas")

        if (self.region=='kedougou'):
            self.lsaraya = self.canvas2.create_text(350,130, text="0 cas")
            self.lkedougou = self.canvas2.create_text(140,140, text="0 cas")
            self.lsalemata = self.canvas2.create_text(110,200, text="0 cas")

        if (self.region=='tambacounda'):
            self.lbakel = self.canvas2.create_text(350,110, text="0 cas")
            self.lgoudiry = self.canvas2.create_text(220,160, text="0 cas")
            self.ltambacounda = self.canvas2.create_text(110,200, text="0 cas")
            self.lkoumpentoun = self.canvas2.create_text(90,110, text="0 cas")
        
        if (self.region=='kolda'):
            self.lvelingara = self.canvas2.create_text(350,130, text="0 cas")
            self.lmedinayoro = self.canvas2.create_text(140,140, text="0 cas")
            self.lkolda = self.canvas2.create_text(110,200, text="0 cas")

        if (self.region=='kaolack'):
            self.lguinguineo = self.canvas2.create_text(156,70, text="0 cas")
            self.lkaolack = self.canvas2.create_text(80,140, text="0 cas")
            self.lnioro = self.canvas2.create_text(110,240, text="0 cas")

        self.canvas2.pack()
    
    def save(self):
        l= self.region+'0.png'
        x=Canvas.winfo_rootx(self.canvas2)
        y=Canvas.winfo_rooty(self.canvas2)
        w=Canvas.winfo_width(self.canvas2  )
        h=Canvas.winfo_height(self.canvas2)
        ImageGrab.grab((x,y,500,500)).save(l)
    
    def don(self):
        date=self.dateDepart
        a=nbrCasParDepartement(self.region, date)
        t=csvDonne(a,date)
        t.csvDepart()
        messagebox.showinfo("Resultat", "Données bien enregistrées")
        
    def create_telcarte_button(self):
        telca = Button(self.frame0, text="Télécharger carte", font=("Courrier", 10), bg='white', fg='#95A5A6',command=self.save)
        telca.pack(side=LEFT,padx=200)
        
    def create_teldonnee_button(self):
        teldon = Button(self.frame0, text="Télécharger Données", font=("Courrier", 10), bg='white', fg='#95A5A6', command=self.don)
        teldon.pack(side=RIGHT,padx=200)


