# Computer linear-regression model trained on tripadvisor ratings data

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn import linear_model

computer_data = pd.read_csv('generate_datasets/computer_model_data.csv')

D=computer_data[['lat','lon','rankingPosition','rankingDenominator','competitors','accessibility','touristic attractions','unattractiveness']]
y=computer_data[['rating']]
regressor= linear_model.LinearRegression()
regressor.fit(D,y)


clustering_data=computer_data[['lat','lon','competitors','accessibility','touristic attractions','unattractiveness','rating']]
cluster_pipe=KMeans(n_clusters=2)
cluster_pipe.fit(clustering_data)
cluster_labels= cluster_pipe.predict(X=clustering_data)
print(silhouette_score(X=clustering_data, labels=cluster_labels, metric='euclidean'))
pca=PCA(n_components=2)
components=pca.fit_transform(clustering_data)
plt.scatter(components[:,0],components[:,1],c=cluster_labels)
print("coefficients of computer model: ",regressor.coef_)
print("cluster score: ",silhouette_score(X=clustering_data, labels=cluster_labels, metric='euclidean'))
print('model score: ', regressor.score(D,y))
print('cluster centroids: ', cluster_pipe.cluster_centers_)
plt.show()


