import os
os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print("Current working directory: {0}".format(os.getcwd()))
import openrouteservice
import folium
import os
import time
from selenium import webdriver
from BFex import bftsp
import pandas as pd
import numpy as np


os.chdir("C:\\Users\\Endrit\\Desktop\\Master Finance\\2nd Semster\\Programming\\ProjectVF\\")
print(os.getcwd())
df = pd.read_excel('10CitiesCH.xlsx', index_col=0)
mat = np.array(df)
cities = df.columns




coordinates =  [(8.539183,47.368650),(6.14234,46.207),(7.5885761,47.5595986),(6.641,46.521),(7.451123,46.947456),
                (8.7251,47.50003),(8.3093072,47.0501682),(9.37477,47.42391),(8.96004,46.01008),(7.2467909,47.1367785)]

swiss = bftsp(mat)
swiss.matdist(coordinates)
swiss.bf(True) # with True it will use the matrix from '10CitiesCH.xlsx'
swiss.bf(False) # with False it will use the matrix computed from the coordinates
minpathkm = swiss.minTourkm
minpath = swiss.minTour

pathcoordkm = [] # we need the coordinate to be in the order of the minpath to plot it
for i in minpathkm:
    pathcoordkm.append(coordinates[i])

pathcoord = [] # we need the coordinate to be in the order of the minpath to plot it
for i in minpath:
    pathcoord.append(coordinates[i])
    
client = openrouteservice.Client(key='*************') # put your personal API key for openrouteservice

route = client.directions(coordinates=pathcoordkm,profile='driving-car',format='geojson')
style1 = {'fillColor': 'lightblue', 'color': 'lightblue'}
map_directions = folium.Map(location=[46.6833 ,7.85],zoom_start=8,tiles=" cartodbpositron",png_enabled=(True))
folium.GeoJson(route, name='route',style_function=lambda x:style1).add_to(map_directions)
folium.LayerControl().add_to(map_directions)


for i in range(len(cities)):
    folium.CircleMarker([coordinates[i][-1],coordinates[i][0]],radius=5,color='cadetblue',fill_color='cadetblue',fill_opacity=0.1,tooltip=cities[i]).add_to(map_directions)

map_directions.save("map_directions.html")

map_directions2 = folium.Map(location=[46.6833 ,7.85],zoom_start=8,tiles=" cartodbpositron",png_enabled=(True))
pathcoordinverse = []
for i in range(len(pathcoord)):
    pathcoordinverse.append((pathcoord[i][-1],pathcoord[i][0]))
    
folium.vector_layers.Polygon(pathcoordinverse,color='lightblue',fill_color='white',fill_opacity=0,weight=3).add_to(map_directions2)
for i in range(len(cities)):
    folium.CircleMarker([coordinates[i][-1],coordinates[i][0]],radius=5,color='cadetblue',fill_color='cadetblue',fill_opacity=0.1,tooltip=cities[i]).add_to(map_directions2)
map_directions2.save("map_directions2.html")




###############################################################################
""""This part of the code is used to open the html link and do screenshot
    if you want to launch this code you need geckodriver.exe to 
    be in your directory"""
delay=5
fn='map_directions.html'
tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)
map_directions.save(fn)

browser = webdriver.Firefox(executable_path= r'C:\Users\Endrit\geckodriver.exe') 
browser.get(tmpurl)
#Give the map tiles some time to load
time.sleep(delay)
browser.save_screenshot('map.png')
browser.quit()


delay=5
fn='map_directions2.html'
tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)
map_directions2.save(fn)
browser = webdriver.Firefox(executable_path= r'C:\Users\Endrit\geckodriver.exe')
browser.get(tmpurl)
#Give the map tiles some time to load
time.sleep(delay)
browser.save_screenshot('map2.png')
browser.quit()
