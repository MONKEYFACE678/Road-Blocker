import requests
import re
import math

class LocationGetter:

    def get_public_ip(self):
        response = requests.get("http://checkip.dyndns.com/")
        response.raise_for_status()
        data = response.text
        ip_address = re.search(r"Address: (\d+\.\d+\.\d+\.\d+)", data)
        if not ip_address:
            raise ValueError("Could not parse public IP from response")
        return ip_address.group(1)

    def get_location_from_ip(self,api_key, ip_address):
        url = f"https://ipinfo.io/{ip_address}/json?token={api_key}"
        response = requests.get(url)
        return response.json()

    def get_location_coordinates(self):
        api_key = "477233b96ca693"
        ip_address = self.get_public_ip()
        location_data = self.get_location_from_ip(api_key, ip_address)
        return 40.7132, -74.0061
    
    def convert_location_to_tile_data(self, lat, lon, zoom):
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
    print(lg.get_location_coordinates())