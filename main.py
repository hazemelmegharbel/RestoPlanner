# Main driver for program

import pandas as pd 
from filter import *
from food_chains import popular_food
OSM_data = pd.read_json('generate_datasets/amenities-vancouver.json', lines=True) 

print("\n~~~ Vancouver Business Planning ~~~\n")

search_again = 'y'
while search_again.lower()=='y':
    search_amenities(OSM_data)
    search_again=input("Would you like to perform another search? (Enter y/n) ")

reselect_amenity = 'y'
while reselect_amenity.lower()=='y':
    selected_am = select_amenity(OSM_data)
    if selected_am!=0: 
        reselect_amenity='n'

if(selected_am!=0):
    find_similar(selected_am)

print("\nWhat location do you plan to set up in?")
lat = float(input("Enter latitude: "))
lon = float(input("Enter longitude: "))
popular_food(OSM_data, lat, lon)
