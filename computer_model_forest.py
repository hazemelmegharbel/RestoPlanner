# Computer random forest regression model trained on tripadvisor ratings data

import ast
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split

def price_transform(str):
    if (str=='$$ - $$$'):
        return 2.5
    elif (str=='$'):
        return 1
    elif(str=='$$$$'):
        return 4

computer_data = pd.read_csv('generate_datasets/computer_model_data.csv')
computer_data['price']=computer_data['priceLevel'].apply(price_transform)
computer_data = computer_data.drop(columns=['Unnamed: 0','priceLevel'])
computer_data = computer_data.dropna()

y=computer_data[['rating']]
D=computer_data.drop(['rating'],axis=1)
y=y.astype(float)
print('Features passed to Random Forest Regressor: ', D.dtypes)
X_train, X_test, y_train, y_test= train_test_split(D,y,test_size=0.33)
regressor= RandomForestRegressor(n_estimators=1000, max_depth=8, min_samples_split=10)

regressor.fit(X_train,y_train)


clustering_data=computer_data[['lat','lon','awards_num', 'price','competitors','accessibility','touristic attractions','unattractiveness','rating']]
cluster_pipe=KMeans(n_clusters=3)
cluster_pipe.fit(clustering_data)
cluster_labels= cluster_pipe.predict(X=clustering_data)
pca=PCA(n_components=2)
components=pca.fit_transform(clustering_data)
plt.scatter(components[:,0],components[:,1],c=cluster_labels)
print("feature importances: ",regressor.feature_importances_)
print("cluster score: ",silhouette_score(X=clustering_data, labels=cluster_labels, metric='euclidean'))
print('model score: ', regressor.score(X_test,y_test))
print('cluster centroids: ', cluster_pipe.cluster_centers_)
plt.savefig('clusters_computer_model.png')
