import numpy as np

print("zadanie 1")
a = float(input("podaj wartość liczby a: "))
b = float(input("podaj wartość liczby b: "))
print(a + b)
print(a * b)
print(a/b)
print(a**b)

print("\n")

print("zadanie 2")
def podwojona(a):
    return a * 2
print(podwojona(1))

print("\n")

print("zadanie 3")

def pierwszy(a):
    return a[1]
print(pierwszy([1, 2, 3, 4, 5]))

print("\n")


print("zadanie 4")

def srodek(a):
    return a[1:4]
print(srodek([1, 2, 3, 4, 5]))


print("\n")


print("zadanie 5")

def najwiekszy(a):
    return np.max(a)
print(najwiekszy([7, 2, 3, 4, 5]))

print("\n")


print("zadanie 6")

def pierwsza_kolumna(a):
    a = np.array(a)
    return a[0][0], a[1][0]
print(pierwsza_kolumna([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]))

print("\n")


print("zadanie 7")

def pierwsza_kolumna_3(a):
    a[:, 0] **= 3
    return a
print(pierwsza_kolumna_3(np.array ([[5, 2, 3, 4, 5], [5, 2, 3, 4, 5]])))



