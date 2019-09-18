# Fish-measurments-
Prediction fish types

Prediction fish types is an unsupervised task. The model chooses the best number of clusters to predict all the fish types in the dataset
based on inertia parameter for KMeans algorithm. The best number of clusters were 4. 

The following table shows the prediction accuracy for every fish type in the dataset without any preprocessing, it has low prediction 
accuracy for Bream and Pike types, while it has hight accuracy for Roach and Smelt types:


Fish types  Bream  Pike  Roach  Smelt
labels                               
0               1     1     17     14
1              16     2      0      0
2              17    10      3      0
3               0     4      0      0


In order to increase the prediction accuracy the dataset has been scaled with zero mean and one standard deviation. The following table
shows the prediction accuracy for every type and how the accuracy is raised:


Fish types     Bream  Pike  Roach  Smelt
scaled labels                           
0                  1     0     19      1
1                  0    17      0      0
2                 33     0      1      0
3                  0     0      0     13
￼
