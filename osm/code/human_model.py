import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn import linear_model
restaurant_data=pd.read_csv('restaurant_data.csv')

def get_score(row):
    return 8*row['touristic attractions'] +0.5*row['competitors'] - 1*row['unattractiveness'] + 5*row['accessibility']

restaurant_data['score']=restaurant_data.apply(lambda row: get_score(row), axis=1)
restaurant_data['normalized']=restaurant_data['score']/np.sum(restaurant_data['score'])
restaurant_data=restaurant_data.drop(['Unnamed: 0','amenity','name','tags','timestamp'], axis=1)

cluster_pipe=KMeans(n_clusters=2)
cluster_pipe.fit(restaurant_data)
cluster_labels= cluster_pipe.predict(X=restaurant_data)
print(silhouette_score(X=restaurant_data, labels=cluster_labels, metric='euclidean'))
pca=PCA(n_components=2)
components=pca.fit_transform(restaurant_data)
plt.scatter(components[:,0],components[:,1],c=cluster_labels)
print("clusters score",silhouette_score(X=restaurant_data, labels=cluster_labels, metric='euclidean'))
print("cluster centers: ", cluster_pipe.cluster_centers_)
plt.show()




