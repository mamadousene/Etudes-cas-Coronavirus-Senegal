from tkinter import *
import  tkinter.ttk as ttk
import  time 
import threading
from tkinter import messagebox
class GUI:
    def __init__(self, master):
        self.master = master
        self.test_button = Button(self.master, command=self.tb_click)
        self.test_button.configure(
            text="Start", background="Grey",
            padx=50
            )
        self.test_button.pack(side=TOP)
    def start_download(self):
        time.sleep(1)
    def progress(self):
        self.prog_bar = ttk.Progressbar(
            self.master, orient="horizontal",
            length=200, mode="indeterminate"
            )
        self.prog_bar.pack(side=TOP)
    def tb_click(self):
        self.progress()
        self.prog_bar.start()
        # Simulate long running process
        t = threading.Thread(target=self.start_download)
        t.start()
        t.start()
        t.join()
root = Tk()
messagebox.showinfo("Info","Fin de Chargement des Tweets depuis twitter")
root.title("Test Button")
main_ui = GUI(root)
root.mainloop()