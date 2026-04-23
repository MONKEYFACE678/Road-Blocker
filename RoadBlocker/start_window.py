'''
-----want to ...
1. eventually add a sound of a car revving up when app begins
-----
2. Move each class to its own file
-----
3. Finish the traffic_window and implement from Trafficgetter, and Location getter files
-----
4. Redesign the labels to look better on ui, Home,search 
instructions, about us, quit
-----
5.
'''
import os as os
import Menu_Window
from tkinter import Frame, PhotoImage, Label, Button, Tk
import PIL
from PIL import Image, ImageTk

class Master_window(Tk):
    
    def __init__(self):
        super().__init__()
        
        #declare resources folder
        dirname = os.path.dirname(__file__)
        self.resources = os.path.join(dirname,"resources")
        
        #title,icon,size
        self.title("ROADBLOCKR")
       
        ico = Image.open('RoadBlocker\\resources\\Icon.png')
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)
        self.geometry('800x650')
        
        self.main_frame = Frame(self)
        #setup for start button, image background, and fonts...
        self.img = PhotoImage(file=os.path.join(self.resources,"start_window.png")).subsample(3)
        self.bg_img = Label(self)
        self.bg_img.image = self.img # type: ignore
        self.bg_img.configure(image = self.bg_img.image) # type: ignore
        self.bg_img.pack(fill="both", expand=True)

        self.title_img = PhotoImage(file = os.path.join(self.resources,"title","title_rb.png")).subsample(2)
        self.title_label = Label(self, image = self.title_img, bg ="#474545",borderwidth=9, relief="raised")
        self.title_label.place(x=80, y=15)
        
        self.start_button = Button(self, text="Start", width=15,height=2,font=('Montserrat', 14), 
        background="#FD8413",relief="flat", command=self.show_main_menu)
        self.start_button.place(x=330, y=539)
        
    def show_main_menu(self):
        Menu_Window.Menu_window(self)
        Menu_Window.Menu_window()
        
    def destroy_window(self):
        self.destroy()





        


 
