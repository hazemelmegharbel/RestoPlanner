# Driver to generate all required datasets

import pandas as pd
from feature_eng import ml_data
from densities import amenity_densities
from food_chains import wiki_foodchains

OSM_data = pd.read_json('amenities-vancouver.json', lines=True) 

ml_data(OSM_data)
amenity_densities(OSM_data)
wiki_foodchains()