from tkinter import Frame, Label, Toplevel

class help_window(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("600x500")