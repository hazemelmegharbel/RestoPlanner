import pandas as pd
from scipy import stats
import numpy as np

def popular_food(OSM_data, lat, lon):
    chains = OSM_data[OSM_data['tags'].apply(lambda tags: 'brand:wikidata' in tags)]
    fast_food = chains[chains['amenity']=='fast_food']
    restaurants = chains[chains['amenity']=='restaurant']

    wiki_df = pd.read_csv('generate_datasets/wiki_foodchains.csv')
    wiki_fast_food = fast_food.merge(wiki_df, on='name')
    wiki_restaurants = restaurants.merge(wiki_df, on='name')

    radius = 0.06
    amenities_in_radius = OSM_data[
    (OSM_data['lat'] > lat-radius) & (OSM_data['lat'] < lat+radius) &
    (OSM_data['lon'] > lon-radius) & (OSM_data['lon'] < lon+radius)
    ]

    xA = wiki_fast_food.merge(amenities_in_radius, on='name')['followers']
    xB = wiki_restaurants.merge(amenities_in_radius, on='name')['followers']

    if (xA.size != 0 & xB.size != 0):
        pvalue_ff= stats.mannwhitneyu(xA, xB, alternative='greater').pvalue
        pvalue_rest= stats.mannwhitneyu(xA, xB, alternative='less').pvalue

        if(pvalue_ff<0.05):
            print("Fast food chains are more popular in this area. Keep low-budget customers in mind.")
        elif(pvalue_rest<0.05):
            print("Restaurant chains are more popular in this area. Keep high-budget customers in mind.")

