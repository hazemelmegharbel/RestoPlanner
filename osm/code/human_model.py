import pandas as pd
import numpy as np
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
restaurant_data=pd.read_csv('restaurant_data.csv')

def get_score(row):
    return 8*row['touristic attractions'] +0.1*row['competitors'] +0.1*row['unattractiveness'] + 3*row['accessibility']

restaurant_data['score']=restaurant_data.apply(lambda row: get_score(row), axis=1)
print(restaurant_data.dtypes)
print(restaurant_data)