from pandas import read_csv, DataFrame
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder

#zbiór_trenujący = read_csv("czy_ryba.csv")
zbiór_trenujący = read_csv("czy_ryba.csv", dtype={"czym_oddycha" : "category"})
print(zbiór_trenujący)
#enc = OrdinalEncoder()
enc = OneHotEncoder(handle_unknown="ignore", sparse_output=False, dtype=int, drop="first")
print(enc)
X_df = zbiór_trenujący.drop(["nazwa", "ryba"], axis=1)
zb_tren = enc.fit_transform(X_df)#zbiór_trenujący)
print(zb_tren)
X = zb_tren
y = zbiór_trenujący.ryba.values
print(f"X = {X}")
print(f"y = {y}")
drzewo = DecisionTreeClassifier()#criterion="entropy")
drzewo.fit(X, y)
#print(["ma_nogi", "ma_płetwy"] + enc.categories_[2].tolist())
print(enc.categories_)
if isinstance(enc, OrdinalEncoder):
    print(export_graphviz(drzewo, out_file="ryba1", feature_names=["ma_nogi", "ma_płetwy", "czym_oddycha"]))
else:
    print(export_graphviz(drzewo, out_file="ryba2", feature_names=["ma_nogi", "ma_płetwy"] + enc.categories_[0].tolist()))

#zbiór_trenujący["czym_oddycha"] = enc.inverse_transform(zbiór_trenujący.czym_oddycha)
print(zbiór_trenujący)

