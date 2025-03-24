import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv('W2.csv')
df = pd.DataFrame(data)

print("Pierwsze 5 wierszy:\n", df.head(5))

print("\nInformacje o DataFrame:")
df.info()

print("\nStatystyki opisowe:\n", df.describe())


missing_values = df.isnull()
print("\nBrakujące dane:\n", missing_values)
df["imie"] = df["imie"].fillna(df["imie"].mode()[0])
missing_values = df.isnull().sum()
print("\nUzupenione dane:\n", missing_values)



unique_val = df["wyksztalcenie"].unique()
print("\n Sprawdzenie kolumny wyksztacenie:\n", unique_val)
df["wyksztalcenie"] = df["wyksztalcenie"].str.strip().str.lower()
unique_val = df["wyksztalcenie"].unique()
print("\nPoprawiona kolumna:\n", unique_val)


df[["wiek", "dochod", "liczba_dzieci"]].boxplot()
plt.show()



unique_gval = df["plec"].unique()
df["plec"] = df["plec"].str.strip().str.lower()
unique_gval = df["plec"].unique()



plt.hist(df["wiek"], bins=10, color='red' )
plt.xlabel("Wiek")
plt.ylabel("Liczba osób")
plt.title("Histogram wieku")
plt.show()


df["liczba_dzieci"].value_counts().sort_index().plot(kind="bar")
plt.xlabel("Liczba dzieci")
plt.ylabel("Liczba osób")
plt.show()


plt.scatter(df["wiek"], df["dochod"], color="green")
plt.xlabel("Wiek")
plt.ylabel("Dochód")
plt.grid(True)
plt.show()


df["plec"].value_counts().plot(kind="pie", colors=["blue", "pink"])
plt.title("Wykres kolorowy")
plt.show()




