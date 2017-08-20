'''
Application 2 - Webmaps with Folium

Generates map using Folium, and reads in data from .txt file about volcanoes in US.
Adds stylized markers to map based on volcano data.
'''

import folium
import pandas

def get_colour(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

data = pandas.read_csv("Volcanoes.txt")
# read data from file and store as lists
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[lat[10], lon[10]], zoom_start=5, tiles="Mapbox Bright")
volcanoG = folium.FeatureGroup(name="Volcanoes")

# loop through data lists to create markers
for lt, ln, el in zip(lat, lon, elev):
    volcanoG.add_child(folium.CircleMarker(location=[lt, ln], popup = str(el) + " m", fill_color=get_colour(el), radius = 6, color="grey"))

map.add_child(volcanoG)
map.save("VolcanoesMap.html")
