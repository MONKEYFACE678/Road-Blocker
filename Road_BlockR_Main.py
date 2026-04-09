import tkinter as tk
from RoadBlocker import TrafficGetter, LocationGetter

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
        "to learn how to design and implement data_windows that can be helpful for students even when they learning how to drive and to test different\n" 
        "traffic management strategies that can be implemented in real life to improve traffic flow and reduce congestion."
    )
    
    tk.Label(about, text=info, font=("Arial", 12), justify="left").pack(padx=20, pady=20)
    
def data_window():
    lg = LocationGetter.LocationGetter()
    tg = TrafficGetter.TrafficGetter()
    data_window = tk.Toplevel(win)
    data_window.title("data_window")
    data_window.geometry("900x500")
    
    def update_data():
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
        data_string.set(f"Current speed in selected area is {current_speed}mph, which is {free_flow_speed- current_speed} mph less than the free flow speed of {free_flow_speed}mph")
    
    data_string = tk.StringVar(data_window, "No Data Currently")
    data_lbl = tk.Label(data_window, textvariable=data_string, font=("Arial", 12), justify="center")
    data_lbl.grid(column=1, row=1)
    
    use_your_loc_button = tk.Button(data_window, text="Use your current location", command=lg.get_location_coordinates_from_ip)
    use_your_loc_button.grid(row=0)
    
    e1 = tk.Entry(data_window)
    e1.insert(0,"Enter Location Here...")
    e1.grid(row=1)
    
    use_entered_loc_button = tk.Button(data_window, text="Submit address", command=lambda:lg.get_location_coordinates_from_address(e1.get()))
    use_entered_loc_button.grid(row=2)
    
    show_data_button =tk.Button(data_window, text="Show data for location", command=update_data)
    show_data_button.grid(column=1)
    

Start_data_window_button = tk.Button(win, text="Get Data", command=data_window)
Start_data_window_button.pack(pady=10)

Settings_button = tk.Button(win, text="Settings", command=lambda: print("Settings"))
Settings_button.pack(pady=10)

#For the the about us screen takes you to a new screen that has information about the project and the team members
About_Us_button = tk.Button(win, text="About Us", command=about_us)
About_Us_button.pack(pady=10)

Quit_button = tk.Button(win, text="Quit", command=win.destroy)
Quit_button.pack(pady=10)

win.mainloop()
