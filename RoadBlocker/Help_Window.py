from tkinter import Frame, Label, Toplevel

class help_window(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")