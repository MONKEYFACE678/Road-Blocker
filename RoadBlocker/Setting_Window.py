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
        self.geometry("400x500")