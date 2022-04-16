# Output datasets containing human-generated features for training regression models

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
    return np.count_nonzero((distance(restaurant, items_) <=402) & (distance(restaurant, items_) > 0))
def get_counts_accessibility(restaurant, items_):
    return np.count_nonzero(distance(restaurant, items_) <=402)
def get_counts_tourism(restaurant, items_):
    return np.count_nonzero(distance(restaurant,items_) <= 2011.68)
def get_counts_unattractive(restaurant, items_):
    return np.count_nonzero(distance(restaurant,items_) <= 402)


def ml_data(amenities_data):
    restaurant_data = amenities_data[amenities_data['amenity']=='restaurant']
    computer_model_data=pd.read_csv('dataset_tripadvisor_clean.csv')

    accessibility_data=amenities_data[(amenities_data['amenity']=='car_sharing') | (amenities_data['amenity']=='ferry_terminal')
    | (amenities_data['amenity']=='bus_station') | (amenities_data['amenity']=='bicycle_rental') | (amenities_data['amenity']=='parking')
    | (amenities_data['amenity']=='parking_space') | (amenities_data['amenity']=='parking_entrance') | (amenities_data['amenity']=='charging_station')]

    tourism_data=pd.read_csv('attractions.csv')
    #compiled this data from https://www.tripadvisor.ca/Attractions-g154943-Activities-oa30-Vancouver_British_Columbia.html
    tourism_data=tourism_data[['lat', 'lon']]

    unattractive_data= amenities_data[(amenities_data['amenity']=='waste_transfer') | (amenities_data['amenity']=='scrapyard') | (amenities_data['amenity']=='sanitary_dump_station') |
                                    (amenities_data['amenity']=='construction') | (amenities_data['amenity']=='waste_disposal')]

    restaurant_data['competitors']=restaurant_data[['lat','lon']].apply(get_counts_competition, items_= restaurant_data, axis=1)
    restaurant_data['accessibility']=restaurant_data[['lat','lon']].apply(get_counts_accessibility, items_=accessibility_data, axis=1)
    restaurant_data['touristic attractions']=restaurant_data[['lat','lon']].apply(get_counts_tourism, items_= tourism_data, axis=1)
    restaurant_data['unattractiveness']=restaurant_data[['lat', 'lon']].apply(get_counts_unattractive, items_=unattractive_data, axis=1)

    computer_model_data['competitors']=computer_model_data[['lat','lon']].apply(get_counts_competition, items_=restaurant_data, axis=1)
    computer_model_data['accessibility']=computer_model_data[['lat','lon']].apply(get_counts_accessibility, items_=restaurant_data, axis=1)
    computer_model_data['touristic attractions']=computer_model_data[['lat','lon']].apply(get_counts_tourism, items_=tourism_data, axis=1)
    computer_model_data['unattractiveness']=computer_model_data[['lat','lon']].apply(get_counts_unattractive, items_=restaurant_data,axis=1)

    restaurant_data.to_csv('restaurant_data.csv')
    computer_model_data.to_csv('computer_model_data.csv')
