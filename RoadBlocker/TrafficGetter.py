import requests
import shutil
import json
from PIL import Image
import LocationGetter
import shutil
import gzip
import mapbox_vector_tile
import math
import os

class TrafficGetter:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.data_folder = os.path.join(dirname,"data")
        os.makedirs(self.data_folder, exist_ok=True)
    
    def save_traffic_image_from_x_y_to_file(self, api_key, x, y, zoom):
        #Requests TomTom api for image
        response = requests.get(f"https://api.tomtom.com/map/1/tile/basic/night/{zoom}/{x}/{y}.png?key={api_key}", stream=True)
        with open(os.path.join(self.data_folder, "map_img.png"), "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        response = requests.get(f"https://api.tomtom.com/traffic/map/4/tile/flow/absolute/{zoom}/{x}/{y}.png?key={api_key}", stream=True)
        with open(os.path.join(self.data_folder, "traffic_img.png"), "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
    
    def show_traffic_image(self):
        #Shows saved image from save_traffic_image_from_x_y_to_file
        image = Image.open(os.path.join(self.data_folder, "traffic_img.png"))
        image.show()
        image = Image.open(os.path.join(self.data_folder, "map_img.png"))
        image.show()
        
    def save_traffic_data_from_coords_to_file(self, api_key, lat, lon, zoom):
        #Requests api for traffic data based on coordinates
        response = requests.get(f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/{zoom}/json?key={api_key}&point={lat},{lon}&unit=mph")
        response.raise_for_status()
        data = response.json()
        
        with open(os.path.join(self.data_folder, "traffic_data.json"), "w",encoding = "utf-8") as out_file:
            json.dump(data, out_file, indent = 2)
        del response
        
    def get_simple_traffic_data_from_file(self):
        #Reads traffic data file, then returns the data simplified
        with open(os.path.join(self.data_folder, "traffic_data.json"), "r") as in_file:
            data = json.load(in_file)["flowSegmentData"]
            current_speed = data["currentSpeed"]
            free_flow_speed = data["freeFlowSpeed"]
            is_road_closure = data["roadClosure"]
            return current_speed, free_flow_speed, is_road_closure
        
    def save_traffic_tile_to_file(self, api_key, x, y, zoom):
        #Requests api for traffic tile based on tile coordinates
        response = requests.get(f"http://api.tomtom.com/map/1/tile/basic/main/{zoom}/{x}/{y}.pbf?key=zTfX7b0hg5V9N5Jzi0bngmq1lFL7vmms", stream=True)
        response.raise_for_status()
        data = response.raw
        
        with open(os.path.join(self.data_folder, "traffic_tile.pbf"), "wb") as out_file:
            shutil.copyfileobj(data, out_file)
        del response
        
    def save_pbf_as_json(self):
        with open(os.path.join(self.data_folder, "traffic_tile.pbf"), "rb") as in_file:
            compressed = in_file.read()

        decompressed = gzip.decompress(compressed)
        tile_bytes = mapbox_vector_tile.decode(decompressed)
        
        with open(os.path.join(self.data_folder, "traffic_tile.json"), "w",encoding = "utf-8") as out_file:
            json.dump(tile_bytes, out_file, indent=2)
            
    def load_tile_data_from_json(self):
        with open(os.path.join(self.data_folder, "tile_data.json"), "r") as in_file:
            data = json.load(in_file)
            
    def save_weighted_graph_from_file_to_file(self):
        with open(os.path.join(self.data_folder, "traffic_tile.json"), "r", encoding="utf-8") as in_file:
            data = json.load(in_file)

        node_map = {}
        graph = {}
        node_id_counter = 0

        def get_node_id(x, y):
            nonlocal node_id_counter
            key = (x, y)
            if key not in node_map:
                node_map[key] = node_id_counter
                node_id_counter += 1
            return node_map[key]

        def distance(x1, y1, x2, y2):
            return math.hypot(x2 - x1, y2 - y1)

        for layer in data.values():
            for feature in layer.get("features", []):
                geom = feature.get("geometry", {})
                props = feature.get("properties", {})

                if geom.get("type") != "LineString":
                    continue

                coords = geom.get("coordinates", [])
                if len(coords) < 2:
                    continue

                for i in range(len(coords) - 1):
                    x1, y1 = coords[i]
                    x2, y2 = coords[i + 1]

                    id1 = get_node_id(x1, y1)
                    id2 = get_node_id(x2, y2)

                    dist = distance(x1, y1, x2, y2)
                    weight = dist

                    graph.setdefault(id1, {})
                    graph.setdefault(id2, {})

                    # keep smallest weight
                    if id2 not in graph[id1] or weight < graph[id1][id2]:
                        graph[id1][id2] = weight
                        graph[id2][id1] = weight

        with open(os.path.join(self.data_folder, "weighted_graph.json"), "w", encoding="utf-8") as out_file:
            json.dump(graph, out_file, indent=2)
        
    def load_weighted_graph_from_file(self):
        with open(os.path.join(self.data_folder, "weighted_graph.json"), "r",encoding = "utf-8") as in_file:
            data = json.load(in_file)  
        graph = data
            
        return graph
                
if __name__ == "__main__":
    lg = LocationGetter.LocationGetter()
    
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
    
    #want to add a way to display text here
    print(f"Current speed in your area is {current_speed}mph, which is {free_flow_speed- current_speed} mph less than the free flow speed of {free_flow_speed}mph")
    if is_road_closed:
        print("However, the road is closed")
        
    tg.save_traffic_tile_to_file(api_key, x, y, zoom)
    tg.save_pbf_as_json()
    tg.save_weighted_graph_from_file_to_file()