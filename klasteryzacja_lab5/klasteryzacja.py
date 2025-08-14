from sklearn.cluster import KMeans, DBSCAN, HDBSCAN, AgglomerativeClustering, OPTICS, AffinityPropagation
from matplotlib.pyplot import scatter, show
from random import random
from numpy import sin, cos, pi
from sys import exit

X = [((random() - 0.5)/10, (random() - 0.5)/10) for _ in range(20)]

#XX = [((random() + 45)/10, (random() - 0.5)/10) for _ in range(20)]
XX = [(2*cos(alfa), 2*sin(alfa)) for alfa in [random() *2*pi for _ in range(200)]]

X += XX

"""x1 = [x[0] for x in X]
x2 = [x[1] for x in X]

scatter(x1, x2)
show()
exit()"""

#klasteryzator = KMeans(n_clusters=4)
#klasteryzator = DBSCAN(eps=0.5, min_samples=4)
#klasteryzator = HDBSCAN(allow_single_cluster=True, cluster_selection_epsilon=0.5, cluster_selection_method="leaf")
klasteryzator = AgglomerativeClustering(n_clusters=7, linkage="single")
#klasteryzator = OPTICS(min_samples=4, max_eps=20.5)
#klasteryzator = AffinityPropagation()

klasteryzator.fit(X)
if hasattr(klasteryzator, "labels_"):
    print(f"Labels: {klasteryzator.labels_}")
if hasattr(klasteryzator, "cluster_centers_"):
    print(f"Centroids: {klasteryzator.cluster_centers_}")
if hasattr(klasteryzator, "components_"):
    print(f"Components: {klasteryzator.components_}")

x1_blue = [x[0] for x, y in zip(X, klasteryzator.labels_) if y == 0]
x2_blue = [x[1] for x, y in zip(X, klasteryzator.labels_) if y == 0]
x1_red = [x[0]  for x, y in zip(X, klasteryzator.labels_) if y == 1]
x2_red = [x[1]  for x, y in zip(X, klasteryzator.labels_) if y == 1]
x1_green = [x[0] for x, y in zip(X, klasteryzator.labels_) if y == 2]
x2_green = [x[1] for x, y in zip(X, klasteryzator.labels_) if y == 2]
x1_yellow = [x[0] for x, y in zip(X, klasteryzator.labels_) if y == 3]
x2_yellow = [x[1] for x, y in zip(X, klasteryzator.labels_) if y == 3]

#print(x1_blue)
#print(x2_blue)
scatter(x1_blue, x2_blue, color="blue")
scatter(x1_red, x2_red, color="red")
scatter(x1_green, x2_green, color="green")
scatter(x1_yellow, x2_yellow, color="yellow")
show()

