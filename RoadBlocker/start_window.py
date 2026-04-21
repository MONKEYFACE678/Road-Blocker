'''
-----want to ...
1. eventually add a sound of a car revving up when app begins
-----
2. Move each class to its own file
-----
3. Finish the traffic_window and implement from Trafficgetter, and Location getter files
-----
4. Redesign the labels to look better on ui, Home,search 
instructions, about us, quit
-----
5.
'''
from tkinter import *
import PIL.Image as im
import PIL.ImageTk as imtk
from PIL import Image
import os as os
import LocationGetter 
import TrafficGetter 

class Master_window(Tk):
    
    def __init__(self):
        super().__init__()
        
        #declare resources folder
        dirname = os.path.dirname(__file__)
        self.resources = os.path.join(dirname,"resources")
        
        #title,icon,size
        self.title("ROADBLOCKR")
        self.iconbitmap("")
        self.geometry('800x650')
        
        self.main_frame = Frame(self)
        #setup for start button, image background, and fonts...
        self.img = PhotoImage(file=os.path.join(self.resources,"start_window.png")).subsample(3)
        self.bg_img = Label(self, image = self.img)
        self.bg_img.pack(fill="both", expand=True)

        self.title_img = PhotoImage(file = os.path.join(self.resources,"title","title_rb.png")).subsample(2)
        self.title_label = Label(self, image = self.title_img, bg ="#474545",borderwidth=9, relief="raised")
        self.title_label.place(x=80, y=15)
        
        self.start_button = Button(self, text="Start", width=15,height=2,font=('Montserrat', 14), 
        background="#FD8413",relief="flat", command=self.show_main_menu)
        self.start_button.place(x=330, y=539)
        
    def show_main_menu(self):
        Menu_window()
        
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
        
        home_btn = Button(self.toggle_menu, text='Home',
                            font=('Bold', 20), bg='#ffb515', fg='white',
                            activebackground='#ffb515', activeforeground='white')
        home_btn.place(x=20, y=20) 
        
        location_search_buttton = Button(self.toggle_menu, text='Search',
                            font=('Bold', 20), bg='#ffb515', fg='white',
                            activebackground='#ffb515', activeforeground='white', command=traffic_data_window)
        location_search_buttton.place(x=20, y=140)
        
        setttings_btn = Button(self.toggle_menu, text='Settings',
                            font=('Bold', 20), bg='#ffb515', fg='white',
                            activebackground='#ffb515', activeforeground='white',)
        setttings_btn.place(x=20, y=80)
        
       
        
        aboutus_btn = Button(self.toggle_menu, text='About us',
                                font=('Bold', 20), bg='#ffb515', fg='white',
                                activebackground='#ffb515', activeforeground='white',command=self.show_about)
        aboutus_btn.place(x=20, y=200)
        
        help_btn = Button(self.toggle_menu, text='Instructions',
                            font=('Bold', 20), bg='#ffb515', fg='white',
                            activebackground='#ffb515', activeforeground='white',command=self.show_help)
        help_btn.place(x=20, y=260)


      
         

        window_height = self.winfo_height()

        self.toggle_menu.place(x=0, y=50, height=window_height, width=200)
        
        self.toggle_button.config(text='⨉')
        self.toggle_button.config(command=collapse_toggle_menu)

    def show_about(self):
            about_us_window()

    def update_data(self):
            traffic_data_window()

    def show_help(self):
            help_window()
    
    

#about us window class, where we talk about all of the team members


class about_us_window(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1500x500")

        self.info = (
                "Road BlockR:\n"
                "This is project that is created to simulate tracfic flows and to test different traffic management strategies.\n"
                "This program was developed by:\n\n" 
                "Jayson Coleman\n" 
                "Angel Carrillo\n"
                "Caden Saiza\n\n"
                "We are all students at the University of New Mexico State Alamorgordo and we created this project as part of our data structures and algorithms class\n"
                "to learn how to design and implement data_windows that can be helpful for students even when they learning how to drive and to test different\n" 
                "traffic management strategies that can be implemented in real life to improve traffic flow and reduce congestion."
            )
            
        self.about_label = Label(self, text=self.info, font=("Montserrat", 14),bg ="#EBF0A4", justify="left")
        self.about_label.pack(padx=20, pady=20)
        
class button_window(Toplevel):
     def __init__(self):
        super().__init__()
        self.geometry("400x500")

class help_window(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
class traffic_data_window(Toplevel):
    
    def __init__(self):
        super().__init__()

        self.geometry("900x600")

        #this is the frame that will hold the image that gets loaded from api, with city label
        bg_frame =Frame(self, bg="lightblue", width=200, height=100, bd=3, relief=RIDGE)
        bg_frame.place(x = 250, y=10, width=600, height=550, anchor='nw')

        city_label = Label()
        city_label.place(anchor='center',x=400, y=10)

        
        lg = LocationGetter.LocationGetter()
        tg = TrafficGetter.TrafficGetter()
            
        api_key = "zTfX7b0hg5V9N5Jzi0bngmq1lFL7vmms"
        lat, lon = lg.current_location
        lat = float(lat)
        lon = float(lon)
        zoom, x, y = lg.convert_location_to_tile_data(lat,lon, 12)
                
        tg.save_traffic_image_from_x_y_to_file(api_key, x, y, zoom)
        
        tg.show_traffic_image()
                    
        tg.save_traffic_data_from_coords_to_file(api_key, lat, lon, zoom)
                    
        current_speed, free_flow_speed, is_road_closed = tg.get_simple_traffic_data_from_file()
                    
        tg.save_traffic_tile_to_file(api_key, x, y, zoom)
        tg.save_pbf_as_json()
        tg.save_weighted_graph_from_file_to_file()
      

      #get the tkinter button stuff to display data
        data_string.set(f"Current speed in selected area is {current_speed} mph, which is {free_flow_speed - current_speed} mph less than the free flow speed of {free_flow_speed} mph")
                
        data_string = StringVar(traffic_data_window
    , "No Data Currently")
        data_lbl = Label(traffic_data_window
    , textvariable=data_string, font=("Arial", 12), justify="center")
        data_lbl.grid(column=1, row=1)
                    
        use_your_loc_button = Button(self, text="Use your current location", command=lg.get_location_coordinates_from_ip)
        use_your_loc_button.place(x=0,y=20)
            
        e1 = Entry(self)
        e1.insert(0,"Enter Location Here...")
        e1.place(x=0,y=50)
            
        use_entered_loc_button = Button(self, text="Submit address", command=lambda:lg.get_location_coordinates_from_address(e1.get()))
        use_entered_loc_button.place(x=0,y=75)
            
        update_data_button = Button(self, text = "Get Data", command = update_data)
        update_data_button.place(x=0,y=100)
 
if __name__ == "__main__":

    start = Master_window()
   
    start.mainloop()