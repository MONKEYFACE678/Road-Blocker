'''
-----want to eventually add a sound of a car revving up when app begins

'''



from tkinter import *
from tkinter import ttk
import PIL.Image as im
import PIL.ImageTk as imtk
from tkinter import filedialog, messagebox
import os as os
import LocationGetter 
import TrafficGetter 


class Master_window(Tk):
    
    def __init__(self):
        super().__init__()
        #title,icon,size
       
       
        self.title("ROADBLOCKR")
        
        self.iconbitmap("")
        self.geometry('800x650')
        
        self.main_frame = Frame(self)
        #setup for start button, image background, and fonts...
        self.img = PhotoImage(file="RoadBlocker\start_window.png").subsample(3)
        self.bg_img = Label(self, image = self.img)
        self.bg_img.pack(fill="both", expand=True)

        self.title_img = PhotoImage(file = "RoadBlocker\\title\\title_rb.png").subsample(2)
        self.title = Label(self, image = self.title_img, bg ="#474545",borderwidth=9, relief="raised")
        self.title.place(x=80, y=15)

        
        self.start_button = Button(self, text="Start", width=15,height=2,font='Montserrat', 
        background="#FD8413",relief="flat", command=self.show_main_menu)
        self.start_button.place(x=330, y=539)
        
    def show_main_menu(self):
        Menu_window()
        

        


class Menu_window(Tk):
    def __init__(self):
        #send super() to Tk 
        super().__init__()
        #title,icon,size 
        self.geometry("800x650")

        About_Us_button = Button(self, text="About Us", command=self.show_about)
        About_Us_button.pack(pady=20)

        Quit_button = Button(self, text="Quit", command=self.destroy)
        Quit_button.pack(pady=50)

        #add the get_traffic_window which will contain the update data function
        #and the widgets associated w that . . .

        
    def show_about(self):
        about_us_window()

    def update_data(self):
        data_window()





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
            
        self.about_label = Label(self, text=self.info, font=("Montserrat", 14),bg ="#F7FF81", justify="left")
        self.about_label.pack(padx=20, pady=20)
        





class data_window(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("900x500")

    def update_data(self):
        
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
        tg.save_pbf_as_json()
        data_string.set(f"Current speed in selected area is {current_speed} mph, which is {free_flow_speed - current_speed} mph less than the free flow speed of {free_flow_speed} mph")
                
        data_string = StringVar(data_window, "No Data Currently")
        data_lbl = Label(data_window, textvariable=data_string, font=("Arial", 12), justify="center")
        data_lbl.grid(column=1, row=1)
                    
      
        
   
      



    
 
if __name__ == "__main__":

    start = Master_window()
    start.mainloop()


 


