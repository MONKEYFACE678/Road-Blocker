#I am attempting to consolidate the code,
#the location and the traffic getter to tkinter setups.
from tkinter import *

class Main_Menu(Tk):
    def __init__(self):
        super().__init__()

        #title,icon,size
        self.title("ROADBLOCKR MAIN MENU")
        #ask caden to design icon for roadblockr
        self.iconbitmap("")
        self.geometry('800x600')


main = Main_Menu()
main.mainloop()
