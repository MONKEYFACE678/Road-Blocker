from tkinter import *
import customtkinter as ct

class settings_window(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.geometry("700x500")
        self.config()
        
        self.toggle_btn = Button(self, text="Light", width=12, relief="raised")
        self.toggle_btn.pack(pady=5)  

    def toggle(self):
        if self.toggle_btn.config('relief')[-1] == 'sunken':
            self.toggle_btn.config(relief="raised")
        else:
            self.toggle_btn.config(relief="sunken")




    def get_dark_mode(self):
        ct.set_appearance_mode("dark")
        pass
    def get_light_mode(self):
        ct.set_appearance_mode("light")
        pass
         