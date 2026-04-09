import tkinter as tk

win = tk.Tk()
win.title("Road BlockR Main Menu")
win.geometry("400x300")

def about_us():
    about = tk.Toplevel(win)
    about.title("About Us")
    about.geometry("1500x500")
    
    info = (
        "Road BlockR:\n"
        "This is project that is created to simulate tracfic flows and to test different traffic management strategies.\n"
        "This program was developed by:\n\n" 
        "Jayson Coleman\n" 
        "Angel Carrillo\n"
        "Caden Saiza\n\n"
        "We are all students at the University of New Mexico State Alamorgordo and we created this project as part of our data structures and algorithms class\n"
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

win.mainloop()
