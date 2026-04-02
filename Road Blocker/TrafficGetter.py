import requests
import shutil
import json
from PIL import Image
from LocationGetter import LocationGetter

class TrafficGetter:
    
    def save_traffic_image_from_x_y_to_file(self, api_key, x, y, zoom):
        #Requests TomTom api for image
        response = requests.get(f"https://api.tomtom.com/traffic/map/4/tile/flow/absolute/{zoom}/{x}/{y}.png?key={api_key}", stream=True)
        with open("traffic_img.png", "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    
    def show_traffic_image(self):
        #Shows saved image from save_traffic_image_from_x_y_to_file
        image = Image.open("traffic_img.png")
        image.show()
        
    def save_traffic_data_from_coords_to_file(self, api_key, lat, lon, zoom):
        #Requests api for traffic data based on coordinates
        response = requests.get(f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/{zoom}/json?key={api_key}&point={lat},{lon}&unit=mph")
        response.raise_for_status()
        data = response.json()
        
        with open("traffic_data.json", "w",encoding = "utf-8") as out_file:
            json.dump(data, out_file, indent = 2)
        del response
        
    def get_simple_traffic_data_from_file(self):
        #Reads traffic data file, then returns the data simplified
        with open("traffic_data.json", "r") as in_file:
            data = json.load(in_file)["flowSegmentData"]
            current_speed = data["currentSpeed"]
            free_flow_speed = data["freeFlowSpeed"]
            is_road_closure = data["roadClosure"]
            return current_speed, free_flow_speed, is_road_closure
                
if __name__ == "__main__":
    lg = LocationGetter()
    address = input("Enter your search location: ")
    location = lg.get_location_coordinates_from_address(address)
    print("Loading...")
    lat, lon = float(location[0]), float(location[1])
    tg = TrafficGetter()
    api_key = "zTfX7b0hg5V9N5Jzi0bngmq1lFL7vmms"
    zoom, x, y = lg.convert_location_to_tile_data(lat,lon, 12)
    tg.save_traffic_image_from_x_y_to_file(api_key, x, y, zoom)
    tg.show_traffic_image()
    tg.save_traffic_data_from_coords_to_file(api_key, lat, lon, zoom)
    current_speed, free_flow_speed, is_road_closed = tg.get_simple_traffic_data_from_file()
    print(f"Current speed in your area is {current_speed}mph, which is {free_flow_speed- current_speed} mph less than the free flow speed of {free_flow_speed}mph")
    if is_road_closed:
        print("However, the road is closed")