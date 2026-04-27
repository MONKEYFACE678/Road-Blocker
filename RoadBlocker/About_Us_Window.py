from tkinter import Label, Toplevel


class about_us_window(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.geometry("1500x500")
        self.config()

        self.info = (
                "Road BlockR:\n"
                "This is project that is created to simulate tracfic flows and to test different traffic management strategies.\n"
                "This program was developed by:\n\n" 
                "Jayson Coleman\n" 
                "Angel Carrillo\n"
                "Caden Saiza\n\n"
                "We are all students at the University\n" 
                 " of New Mexico State Alamorgordo and we \n" 
                 "created this project as part of our data structures and algorithms class \n"
                "to learn how to design and implement data_windows that can be helpful for students \n"
                 " even when they learning how to drive and to test different\n" 
                "traffic management strategies that can be implemented in real life to \n"
                "improve traffic flow and reduce congestion."
            )
            
        self.about_label = Label(self, text=self.info, font=("Montserrat", 14),bg ="#B0B0B0", justify="left")
        self.about_label.pack(padx=20, pady=20)