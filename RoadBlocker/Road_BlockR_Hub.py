import tkinter as tk

root = tk.Tk()
root.geometry('300x500')
root.title('Road BlockR Hub')

def toggle_menu():
    
    def collapse_toggle_menu():
        toggle_menu_fm.destroy()
        toggle_btn.config(text='≡')
        toggle_btn.config(command=toggle_menu)

    toggle_menu_fm = tk.Frame(root, bg='#ffb515')
    
    home_btn = tk.Button(toggle_menu_fm, text='Home',
                         font=('Bold', 20), bg='#ffb515', fg='white',
                         activebackground='#ffb515', activeforeground='white',)
    home_btn.place(x=20, y=20)
    
    setttings_btn = tk.Button(toggle_menu_fm, text='Settings',
                              font=('Bold', 20), bg='#ffb515', fg='white',
                              activebackground='#ffb515', activeforeground='white',)
    setttings_btn.place(x=20, y=80)
    
    cities_btn = tk.Button(toggle_menu_fm, text='Cities',
                           font=('Bold', 20), bg='#ffb515', fg='white',
                           activebackground='#ffb515', activeforeground='white',)
    cities_btn.place(x=20, y=140)
    
    aboutus_btn = tk.Button(toggle_menu_fm, text='About Us',
                            font=('Bold', 20), bg='#ffb515', fg='white',
                            activebackground='#ffb515', activeforeground='white',)
    aboutus_btn.place(x=20, y=200)
    
    help_btn = tk.Button(toggle_menu_fm, text='Help',
                         font=('Bold', 20), bg='#ffb515', fg='white',
                         activebackground='#ffb515', activeforeground='white',)
    help_btn.place(x=20, y=260)


    window_height = root.winfo_height()

    toggle_menu_fm.place(x=0, y=50, height=window_height, width=200)
    
    toggle_btn.config(text='⨉')
    toggle_btn.config(command=collapse_toggle_menu)

head_frame = tk.Frame(root, bg="#ffb515",
                      highlightbackground='white', highlightthickness=1)

toggle_btn = tk.Button(head_frame, text='≡', bg="#ca8d09", fg='white', 
                       font=('Bold', 20), bd=0,
                       activebackground="#ca8d09", activeforeground='white', 
                       command=toggle_menu)

toggle_btn.pack(side=tk.LEFT)

title_lb = tk.Label(head_frame, text='Road BlockR Hub', bg="#ffb515", fg='white',
                    font=('Bold', 20))

title_lb.pack(side=tk.LEFT)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)




root.mainloop()
