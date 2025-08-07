from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer

from matplotlib.pyplot import scatter, plot, show


dataset = load_breast_cancer()
X = dataset.data
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y)


drzewo = DecisionTreeClassifier(max_leaf_nodes=8)#max_depth=4)

drzewo.fit(X_train, y_train)

print("Dla zbioru trenującego:")

yy = drzewo.predict(X_train)
diff = [e1 - e2 for e1, e2 in zip(yy, y_train)]
norm = sum([e if e >=0 else -e for e in diff])
print(diff, norm)

print("Dla zbioru testowego:")

y = drzewo.predict(X_test)
diff = [e1 - e2 for e1, e2 in zip(y, y_test)]
norm = sum([e if e >=0 else -e for e in diff])
print(diff, norm)

graf = export_graphviz(drzewo, out_file="drzewo-br_canc.txt", feature_names=dataset.feature_names)

