import pandas as pd
import numpy as np

def distance(restaurant,items):
    r = 6371
    lat1 = restaurant['lat']
    lon1 = restaurant['lon']
    lat2 = items['lat']
    lon2 = items['lon']

    lat_subtraction = lat2 - lat1
    lon_subtraction = lon2 - lon1
    var1 = (np.sin((1 / 2 * lat_subtraction) * np.pi / 180)) ** 2
    var3 = (np.sin(np.pi / 180 * (1 / 2 * lon_subtraction))) ** 2
    var2 = np.cos(lat1 * np.pi / 180) * np.cos(lat2 * np.pi / 180) * var3
    total = var1 + var2
    total2 = np.sqrt(total)
    final = 2 * r * np.arcsin(total2)
    return (final * (10 ** 3))

def get_counts_competition(restaurant, items_):
    return np.count_nonzero((distance(restaurant, items_) <=406) & (distance(restaurant, items_) > 0))
def get_counts_accessibility(restaurant, items_):
    return np.count_nonzero(distance(restaurant, items_) <=406)
def get_counts_tourism(restaurant, items_):
    return np.count_nonzero(distance(restaurant,items_) <= 813)




amenities_data= pd.read_json('/osm/amenities-vancouver.json.gz',
                             compression='gzip', lines=True)


restaurant_data = amenities_data[amenities_data['amenity']=='restaurant']

accessibility_data=amenities_data[(amenities_data['amenity']=='car_sharing') | (amenities_data['amenity']=='ferry_terminal')
| (amenities_data['amenity']=='bus_station') | (amenities_data['amenities']=='bicycle_rental') | (amenities_data['amenity']=='parking')
| (amenities_data['amenity']=='parking_space') | (amenities_data['amenity']=='parking_entrance') | (amenities_data['amenity']=='charging_station')]

restaurant_data['competitors']=restaurant_data[['lat','lon']].apply(get_counts_competition, items_= restaurant_data, axis=1)
restaurant_data['accessibility']=restaurant_data[['lat','lon']].apply(get_counts_accessibility, items_=accessibility_data, axis=1)

print(amenities_data['tags'].iloc[0])