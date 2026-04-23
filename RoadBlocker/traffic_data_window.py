import LocationGetter
import TrafficGetter
from tkinter import Frame, Label, Button,StringVar,Entry, Toplevel, RIDGE, PhotoImage
import os
from PIL import Image, ImageTk

class traffic_data_window(Toplevel):
    
    def __init__(self):
        super().__init__()
        
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
        bg_frame =Frame(self, bg="lightblue", width=200, height=100, bd=3, relief=RIDGE)
        self.satelite_img = PhotoImage()
        self.satelite_img_lbl = Label(bg_frame)
        self.satelite_img_lbl.pack(fill="both", expand=True) 
        bg_frame.place(x = 250, y=10, width=600, height=550, anchor='nw')

        city_label = Label()
        city_label.place(anchor='center',x=400, y=10)
        
        data_string = StringVar(self, "No Data Currently")
        data_lbl = Label(self, textvariable=data_string, font=("Arial", 12), justify="center")
        data_lbl.place(x=0,y=0)
                    
        use_your_loc_button = Button(self, text="Use your current location", command=lg.get_location_coordinates_from_ip)
        use_your_loc_button.place(x=0,y=20)
            
        e1 = Entry(self)
        e1.insert(0,"Enter Location Here...")
        e1.place(x=0,y=50)
            
        use_entered_loc_button = Button(self, text="Submit address", command=lambda:lg.get_location_coordinates_from_address(e1.get()))
        use_entered_loc_button.place(x=0,y=75)
            
        update_data_button = Button(self, text = "Get Data", command = update_data)
        update_data_button.place(x=0,y=100)