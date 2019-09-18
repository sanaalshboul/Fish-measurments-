# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:09:42 2019

@author: Administrator
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


plt.style.use('ggplot')

fish=pd.read_csv('C:\\Users\\Administrator.Omnisec421_05\\Downloads\\Fish measurements.csv', header=None)

target=fish[0]

target=np.array(target)

fish=fish.drop(0, axis=1)

k_list=[]
inertia_list=[]
for i in range (1,10):

    model = KMeans(n_clusters=i)
    model.fit(fish)
    
    labels = model.predict(fish)
    k_list.append(i)
    inertia_list.append(model.inertia_)
    
plt.plot(k_list,inertia_list, marker='.')
plt.xlabel('Number of clusters')
plt.ylabel('inertia')
plt.show()


model = KMeans(n_clusters=4)
model.fit(fish)
labels = model.predict(fish)
    
df=pd.DataFrame({'labels': labels, 'Fish types':target})
ct=pd.crosstab(df['labels'], df['Fish types'])
print(ct)

#print(fish.var())


#######################
scaler=StandardScaler()
scaler.fit(fish)
StandardScaler(copy=True, with_mean=True, with_std=True)

sampled_scale=scaler.transform(fish)

scaler_df=pd.DataFrame(sampled_scale)

#print(scaler_df.var())

#######################
model_scale = KMeans(n_clusters=4)
model_scale.fit(sampled_scale)
labels_scale = model_scale.predict(sampled_scale)
    
df=pd.DataFrame({'scaled labels': labels_scale, 'Fish types':target})

print()
print('fish type prediction after scaling the dataset: ')
print()
ct_scale=pd.crosstab(df['scaled labels'], df['Fish types'])
print(ct_scale)

