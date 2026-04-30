import os as os

from About_Us_Window import about_us_window
from Help_Window import help_window
from Setting_Window import settings_window
from Traffic_Data_Window import traffic_data_window
from tkinter import Frame, Label, Button, Toplevel, LEFT, TOP, X
import os

class Menu_window(Toplevel):
    def __init__(self, master):
        #send super() to Tk 
        super().__init__(master)
        self.master = master
        #title,icon,size 
        self.geometry("300x500")
        self.config()
        
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
                            activebackground='#ffb515', activeforeground='white', command=lambda:traffic_data_window(self))
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
                        activebackground='#ffb515', activeforeground='white', command=self.exit)
        quit_btn.place(x=20, y=260)

        window_height = self.winfo_height()

        self.toggle_menu.place(x=0, y=50, height=window_height, width=200)
        
        self.toggle_button.config(text='⨉')
        self.toggle_button.config(command=collapse_toggle_menu)

    def show_about(self):
        about_us_window(self)

    def show_help(self):
        help_window(self)

    def show_settings(self):
        settings_window(self)
        
    def exit(self):
        self.master.destroy()