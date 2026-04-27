from tkinter import Frame, Label, Toplevel
from tkinter import *

class help_window(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.geometry("600x500")
        self.config()