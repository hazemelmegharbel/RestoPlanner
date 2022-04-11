import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
restaurant_data=pd.read_csv('restaurant_data.csv')

def get_score(row):
    return 20*row['touristic attractions'] - 15*row['competitors'] -10*row['unattractiveness'] +10*row['accessibility']

restaurant_data['score']=restaurant_data.apply(lambda row: get_score(row), axis=1)
print(restaurant_data)