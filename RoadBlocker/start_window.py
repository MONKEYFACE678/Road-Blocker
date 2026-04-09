# This is a traffic simulation main menu screen that I'm going to construct
# The main menu will have the following options such as Start simulation settings about US credits and a quit button
# I will be using tkinter to create the main menu screen and import the buttons that will hav mouse interaction and will be able to click on the buttons to navigate to different screens such as the settings screen and the about us screen

from tkinter import *


import PIL.Image as im
import PIL.ImageTk as imtk


from tkinter import filedialog, messagebox

import rembg
import io
import os
import tempfile
import shutil
from tkinterdnd2 import TkinterDnD, DND_FILES


class Windows_Frames(Tk):
    def __init__(self):
        super().__init__()

        #title,icon,size
        self.title("ROADBLOCKR MAIN MENU")
    
        self.iconbitmap("")
        self.geometry('800x650')
        

    #remove background image from png text, starting frame, and start button 
    # and displayfonts. . .
     
   

    def start_frame(self):
        self.start_frame = Frame(self, width=800,height=650)
        #setup for start button, image background, and fonts...
        self.img = PhotoImage(file="RoadBlocker\start_window.png").subsample(3)
        self.bg_img = Label(self, image = self.img)
        self.bg_img.pack(fill="both", expand=True)

        self.start_button = Button(self, text="Start", width=15,height=2,font='helvetica', 
        background="#F9881F",relief="flat")
        self.start_button.place(x=330, y=539)
        

    def display_title(self):
        pass
       
       



    def main_menu_frame(self):
        pass


      


    
 


start = Windows_Frames()

start.start_frame()

start.display_title()
start.mainloop()
 


