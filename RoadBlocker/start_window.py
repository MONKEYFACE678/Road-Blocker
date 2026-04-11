from tkinter import *

from tkinter import ttk
import PIL.Image as im
import PIL.ImageTk as imtk
from tkinter import filedialog, messagebox
import os as os


class Master_Frame(Tk):
    
    def __init__(self):
        super().__init__()
        #title,icon,size
       
       
        self.title("ROADBLOCKR")
        
        self.iconbitmap("")
        self.geometry('800x650')
        
        self.main_frame = Frame(self)
        #setup for start button, image background, and fonts...
        self.img = PhotoImage(file="RoadBlocker\start_window.png").subsample(3)
        self.bg_img = Label(self, image = self.img)
        self.bg_img.pack(fill="both", expand=True)

        self.title_img = PhotoImage(file = "RoadBlocker\\title\\title_rb.png").subsample(2)
        self.title = Label(self, image = self.title_img, bg ="#474545",borderwidth=9, relief="raised")
        self.title.place(x=80, y=15)

        
        self.start_button = Button(self, text="Start", width=15,height=2,font='Montserrat', 
        background="#FD8413",relief="flat", command=self.show_main_menu)
        self.start_button.place(x=330, y=539)
        
    def show_main_menu(self):
        Menu_window()
        

        


class Menu_window(Tk):
    def __init__(self):
        #send master to toplevel from super() class 
        super().__init__()
        #title,icon,size 
        self.geometry("800x650")

        About_Us_button = Button(self, text="About Us", command=self.show_about)
        About_Us_button.pack(pady=10)

        Quit_button = Button(self, text="Quit", command=self.destroy)
        Quit_button.pack(pady=10)
        
    def show_about(self):
        about_us_window()

class about_us_window(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1500x500")

        self.info = (
                "Road BlockR:\n"
                "This is project that is created to simulate tracfic flows and to test different traffic management strategies.\n"
                "This program was developed by:\n\n" 
                "Jayson Coleman\n" 
                "Angel Carrillo\n"
                "Caden Saiza\n\n"
                "We are all students at the University of New Mexico State Alamorgordo and we created this project as part of our data structures and algorithms class\n"
                "to learn how to design and implement data_windows that can be helpful for students even when they learning how to drive and to test different\n" 
                "traffic management strategies that can be implemented in real life to improve traffic flow and reduce congestion."
            )
            
        self.about_label = Label(self, text=self.info, font=("Arial", 12), justify="left").pack(padx=20, pady=20)
        

    

   


      


    
 
if __name__ == "__main__":

    start = Master_Frame()
   
   
    
    start.mainloop()


 


