import pandas as pd 
from filter import search_amenities
OSM_data = pd.read_json('amenities-vancouver.json', lines=True) 

print("\n~~~ Vancouver Business Planning ~~~\n")

search_amenities(OSM_data)