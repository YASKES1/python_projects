import matplotlib.pyplot as plt
plt.style.available

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]


#стилі
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

#поставити точку на графіку на координатах (2,4)
#ax.scatter(2, 4, s=200)

ax.scatter(x_values,y_values, s=100)

# задати назву для графіка кожної осей

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#задати розмір шрифту підписів
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()