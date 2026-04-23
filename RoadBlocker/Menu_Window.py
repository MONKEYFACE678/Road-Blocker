import os as os
import traffic_data_window
import About_Us_Window
import Help_Window
from tkinter import Frame, Label, Button, Toplevel, LEFT, TOP, X
import os
import Setting_Window
import start_window

class Menu_window(Toplevel):
    def __init__(self):
        #send super() to Tk 
        super().__init__()
        #title,icon,size 
        self.geometry("300x500")
        
        self.head_frame = Frame(self, bg="#ffb515",
                    highlightbackground='white', highlightthickness=1)

        self.toggle_button = Button(self.head_frame, text='≡', bg="#ca8d09", fg='white', 
                    font=('Bold', 20), bd=0,
                    activebackground="#ca8d09", activeforeground='white', 
                    command=self.toggle_menu_open)

        self.toggle_button.pack(side=LEFT)

        self.title_lb = Label(self.head_frame, text='Road BlockR Hub', bg="#ffb515", fg='white',
                font=('Bold', 20))

        self.title_lb.pack(side=LEFT)

        self.head_frame.pack(side=TOP, fill=X)
        self.head_frame.pack_propagate(False)
        self.head_frame.configure(height=50)
        
    def toggle_menu_open(self):
        
        def collapse_toggle_menu():
            self.toggle_menu.destroy()
            self.toggle_button.config(text='≡')
            self.toggle_button.config(command=self.toggle_menu_open)

        self.toggle_menu = Frame(self, bg='#ffb515')
        
    
        
        location_search_buttton = Button(self.toggle_menu, text='Search',
                            font=('Bold', 20), bg='#ffb515', fg='white',
                            activebackground='#ffb515', activeforeground='white', command=traffic_data_window.traffic_data_window)
        location_search_buttton.place(x=20, y=20)
        
        setttings_btn = Button(self.toggle_menu, text='Settings',
                            font=('Bold', 20), bg='#ffb515', fg='white',
                            activebackground='#ffb515', activeforeground='white',command=self.show_settings)
        setttings_btn.place(x=20, y=80)
        
        aboutus_btn = Button(self.toggle_menu, text='About us',
                                font=('Bold', 20), bg='#ffb515', fg='white',
                                activebackground='#ffb515', activeforeground='white',command=self.show_about)
        aboutus_btn.place(x=20, y=140)
        
        help_btn = Button(self.toggle_menu, text='Instructions',
                            font=('Bold', 20), bg='#ffb515', fg='white',
                            activebackground='#ffb515', activeforeground='white',command=self.show_help)
        help_btn.place(x=20, y=200)


        quit_btn = Button(self.toggle_menu, text='Quit', font=('Bold', 20), bg='#ffb515',fg='white',
                        activebackground='#ffb515', activeforeground='white')
        quit_btn.place(x=20, y=260)
         

        window_height = self.winfo_height()

        self.toggle_menu.place(x=0, y=50, height=window_height, width=200)
        
        self.toggle_button.config(text='⨉')
        self.toggle_button.config(command=collapse_toggle_menu)

    def show_about(self):
        About_Us_Window.about_us_window()

    def show_help(self):
        Help_Window.help_window()

    def show_settings(self):
        Setting_Window.settings_window()

