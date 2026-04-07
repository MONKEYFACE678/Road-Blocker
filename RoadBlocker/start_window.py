# This is a traffic simulation main menu screen that I'm going to construct
# The main menu will have the following options such as Start simulation settings about US credits and a quit button
# I will be using tkinter to create the main menu screen and import the buttons that will hav mouse interaction and will be able to click on the buttons to navigate to different screens such as the settings screen and the about us screen

from tkinter import *
import PIL.Image as im
import PIL.ImageTk as imtk




class Windows_Frames(Tk):
    def __init__(self):
        super().__init__()

        #title,icon,size
        self.title("ROADBLOCKR MAIN MENU")
        #ask caden to design icon for roadblockr
        self.iconbitmap("")
        self.geometry('800x650')
        
        
    def start_frame(self):
        #setup for start button, image background...
        self.img = PhotoImage(file="RoadBlocker\start_window.png").subsample(3)
        self.bg_img = Label(self, image = self.img)
        self.bg_img.pack(fill="both", expand=True)

        
        
        self.start_button = Button(self, text="Start", width=10,height=2,font="helvetica", background="Orange")
        self.start_button.place(x=360, y=541)

    def display_fonts(self):
        self.letter_r = PhotoImage(file="RoadBlocker/tire_r.png").subsample(18)
        self.r = Label(self,image = self.letter_r)
        self.r.place(x=30,y=30)

    def main_menu_frame(self):
        pass


      


    
 

'''
        def about_us():
        about = Main_Menu.Toplevel(win)
        about.title("About Us")
        about.geometry("500x350")
        
        info = (
            "Road BlockR:\n"
            "This is project that is created to simulate tracfic flows and to test different traffic management strategies.\n"
            "This program was developed by:\n\n" 
            "Jayson Coleman\n" 
            "Angel Carrillo\n"
            "Caden Saiza\n\n"
            "We are all students at the Univeristy of New Mexico State Alamorgordo and we created this project as part of our computer science class\n"
            "to learn how to design and implement simulations that can be helpful for students even when they learning how to drive and to test different\n" 
            "traffic management strategies that can be implemented in real life to improve traffic flow and reduce congestion."
        )
        
        tk.Label(about, text=info, font=("Arial", 12), justify="left").pack(padx=20, pady=20)

    Start_Simulation_button = tk.Button(win, text="Start Simulation", command=lambda: print("Start Simulation"))
    Start_Simulation_button.pack(pady=10)

    Settings_button = tk.Button(win, text="Settings", command=lambda: print("Settings"))
    Settings_button.pack(pady=10)

    #For the the about us screen takes you to a new screen that has information about the project and the team members
    About_Us_button = tk.Button(win, text="About Us", command=about_us)
    About_Us_button.pack(pady=10)

    Quit_button = tk.Button(win, text="Quit", command=win.destroy)
    Quit_button.pack(pady=10)
    '''

start = Windows_Frames()
start.start_frame()
start.display_fonts()
start.mainloop()
 


