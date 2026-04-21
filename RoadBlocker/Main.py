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
import Help_Window
import Setting_Window
import start_window

if __name__ == "__main__":

    start = start_window.Master_window()
   
    start.mainloop()