import requests
import re
import math

class LocationGetter:
    def __init__(self):
        self.current_location = 0,0

    def get_public_ip(self):
        #Gets IP
        response = requests.get("http://checkip.dyndns.com/")
        response.raise_for_status()
        data = response.text
        #Uses regex to parse response text for ip address
        ip_address = re.search(r"Address: (\d+\.\d+\.\d+\.\d+)", data)
        if not ip_address:
            raise ValueError("Could not parse public IP from response")
        return ip_address.group(1)

    def get_location_from_ip(self, api_key, ip_address):
        #Uses ip address to get location
        url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"
        response = requests.get(url)
        return response.json()

    def get_location_coordinates_from_ip(self):
        #Gets ip
        api_key = "477233b96ca693"
        ip_address = self.get_public_ip()
        #Then gets coordinates from ip
        location_data = self.get_location_from_ip(api_key, ip_address)
        self.current_location = location_data["loc"].split(",")
        return location_data["loc"].split(",")
    
    def get_location_coordinates_from_address(self, address):
        #Make an api call to tomtom for geocoding the address
        api_key = "zTfX7b0hg5V9N5Jzi0bngmq1lFL7vmms"
        url = f"https://api.tomtom.com/search/2/geocode/{address}.json?key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data["results"] is None:
            raise RuntimeError("No results found")
        location = data["results"][0]["position"]
        self.current_location = [location["lat"], location["lon"]]
        return [location["lat"], location["lon"]]
    
    def convert_location_to_tile_data(self, lat, lon, zoom):
        #Converts coordinates to tiles system. Annoying sphere math
        MIN_ZOOM = 0
        MAX_ZOOM = 22
        MIN_LAT = -85.051128779807
        MAX_LAT = 85.051128779806
        MIN_LON = -180.0
        MAX_LON = 180.0
        
        if zoom < MIN_ZOOM or zoom > MAX_ZOOM:
            raise ValueError("Zoom level out of range")
        
        if lat < MIN_LAT or lat > MAX_LAT:
            raise ValueError("Lat out of range")
        
        if lon < MIN_LON or lon > MAX_LON:
            raise ValueError("Lon out of range")
        
        xyTileCount = 2**zoom
        x = int(((lon + 180) / 360) * xyTileCount)
        y = int(((1-math.log(math.tan((lat * math.pi)/180)+1/math.cos((lat*math.pi)/180))/math.pi)/2)*xyTileCount)
        
        return (zoom, x, y)
        
if __name__ == "__main__":
    lg = LocationGetter()
    print(lg.get_location_coordinates_from_ip())