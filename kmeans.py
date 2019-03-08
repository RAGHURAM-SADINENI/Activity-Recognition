import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.DataFrame({'x':[12,20,28,18,29,33,24,45,52,51,52,55,53,61,64,69,72],
                 'y':[39,36,30,52,54,46,55,59,63,70,66,63,58,23,14,8,19]
                 })
kmeans=KMeans(n_clusters=3)
kmeans.fit(df)
labels=kmeans.predict(df)
centroids=kmeans.cluster_centers_
print(labels)

fig=plt.figure(figsize=(5,5))

plt.scatter(df['x'],df['y'],edgecolor='k')
for idx,centroid in enumerate(centroids):
    plt.scatter(*centroid)
plt.xlim(0,80)
plt.ylim(0,80)
plt.show()

