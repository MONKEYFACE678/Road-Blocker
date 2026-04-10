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
        menu = Menu(self)

        


class Menu(Toplevel):
    def __init__(self, master):
        #send master to toplevel from super() class 
        super().__init__(master)
        #title,icon,size
        self.menu_frame = Frame(self)
        self.pack(fill="both", expand = True)

        lbl = Label(self.menu_frame, text ="gggfdgsfdg  ")
        
    

   


      


    
 
if __name__ == "__main__":

    start = Master_Frame()
   
    
    start.mainloop()


 


