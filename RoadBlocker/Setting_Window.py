from tkinter import *
import customtkinter as ct

class settings_window(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("700x500")
        
    def toggle(self):
        toggle_btn = Button(text="Toggle", width=12, relief="raised")
        toggle_btn.pack(pady=5)    

    def get_dark_mode(self):
        ct.set_appearance_mode("dark")
        pass
    def get_light_mode(self):
        ct.set_appearance_mode("light")
        pass
         