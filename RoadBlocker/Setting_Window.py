from tkinter import *
import PIL.Image as im
import PIL.ImageTk as imtk
from PIL import Image
import os as os
import LocationGetter 
import TrafficGetter 
import traffic_data_window
import Menu_Window
import About_Us_Window
from tkinter import Frame, Label, Button,StringVar,Entry, Toplevel, RIDGE, PhotoImage
import os
import start_window


class settings_window(Toplevel):
     def __init__(self):
        super().__init__()
        self.geometry("1000x500")
    
     
        stats = Label(self, text="Stats Setting", font=("Arial", 16))
        stats.place(x=20, y=50)
        density = Label(self, text="Traffic Density:", font=("Arial", 12))
        density.place(x=20, y=75)
        density_var = StringVar(value="Medium")
        
        option_menu = OptionMenu(self, density_var, "Low", "Medium", "High")
        option_menu.place(x=20, y=100)

        save = Button(self, text="Save Settings", command=lambda: print(f" Density: {self.density_var.get()}"))
        save.place(x=20, y=150)