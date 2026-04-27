import LocationGetter
import TrafficGetter
from tkinter import Frame, Label, Button,StringVar,Entry, Toplevel, RIDGE, PhotoImage, END
import os
from PIL import Image, ImageTk

class traffic_data_window(Toplevel):
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(bg="#1D86CC")

       

        def update_data():
            api_key = "zTfX7b0hg5V9N5Jzi0bngmq1lFL7vmms"
            
            lat, lon = lg.current_location
            lat = float(lat)
            lon = float(lon)
            zoom, x, y = lg.convert_location_to_tile_data(lat,lon, 12)
                    
            tg.save_traffic_image_from_x_y_to_file(api_key, x, y, zoom)
                                    
            tg.save_traffic_data_from_coords_to_file(api_key, lat, lon, zoom)
                        
            current_speed, free_flow_speed, is_road_closed = tg.get_simple_traffic_data_from_file()
                        
            tg.save_traffic_tile_to_file(api_key, x, y, zoom)
            tg.save_pbf_as_json()
            tg.save_weighted_graph_from_file_to_file()
            
            map_img_path = os.path.join(self.data_folder, "map_img.png")
            traffic_img_path = os.path.join(self.data_folder, "traffic_img.png")
            
            map_img = Image.open(map_img_path).convert("RGBA")
            traffic_img = Image.open(traffic_img_path).convert("RGBA")
            
            map_img = map_img.resize((500,500))

            traffic_img = traffic_img.resize(map_img.size)

            traffic_img.putalpha(128)  # 128 = 50% transparency

            combined = Image.alpha_composite(map_img, traffic_img)

            self.satelite_img = ImageTk.PhotoImage(combined)

            self.satelite_img_lbl.config(image=self.satelite_img)
            self.satelite_img_lbl.image = self.satelite_img # type: ignore
            
            data_string.set(f"Current speed in selected area is {current_speed} mph, which is {free_flow_speed - current_speed} mph less than the free flow speed of {free_flow_speed} mph")
    
        def clear_entry(event, entry):
            entry.delete(0, END)
    
        lg = LocationGetter.LocationGetter()
        tg = TrafficGetter.TrafficGetter()
        dirname = os.path.dirname(__file__)
        self.data_folder = os.path.join(dirname,"data")
        
        #Do this
        #os.path.join(self.data_folder, "traffic_img.png")
        
        #Instead of this
        #"Road Blocker\RoadBlocker\data\traffic_img.png"

        self.geometry("900x600")

        #this is the frame that will hold the image that gets loaded from api, with city label
        bg_frame =Frame(self, bg="#E19507", width=200, height=100, bd=7, relief=RIDGE)
        self.satelite_img = PhotoImage()
        self.satelite_img_lbl = Label(bg_frame, bg="#2B00C8")
        self.satelite_img_lbl.pack(fill="both", expand=True) 
        bg_frame.place(x = 250, y=10, width=600, height=550, anchor='nw')

        city_label = Label()
        city_label.place(anchor='center',x=400, y=10)
        
        data_string = StringVar(self, "No Data Currently")
        data_lbl = Label(self, textvariable=data_string, font=("Arial", 14), justify="center")
        data_lbl.place(x=0,y=10)
        
        #this is where i have the current location also get data without hacing to press 2 buttons
        def get_data_from_current():
            lg.get_location_coordinates_from_ip()
            update_data()

        #this is so the user doesn't have to select address as well as update data...
        def get_data_from_search():
            lg.get_location_coordinates_from_address(e1.get())
            update_data()

        use_your_loc_button = Button(self, relief = "raised",bg="#EAE0C3", text="My location",font=('Arial',12 ),command=get_data_from_current)
        use_your_loc_button.place(x=30, y=100)
            
        e1 = Entry(self, font=('Ariel',12 ))
        e1.insert(0,"Enter Location Here...")
        e1.place(x=30,y=140)
        
        e1.bind("<Button-1>", lambda event: clear_entry(event, e1))
            
        use_entered_loc_button = Button(self, relief="raised",text="Submit address",bg="#EAE0C3", font=('Arial',12 ),command= get_data_from_search)
        use_entered_loc_button.place(x=30,y=170)
            
        
       