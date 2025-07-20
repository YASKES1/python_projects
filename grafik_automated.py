import matplotlib.pyplot as plt
plt.style.available

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


#стилі
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

#поставити точку на графіку на координатах (2,4)
#ax.scatter(2, 4, s=200)

ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# задати назву для графіка кожної осей

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#задати розмір шрифту підписів
ax.tick_params(axis='both', which='major', labelsize=14)

#задати діпазон для кожної з осей
ax.axis([0, 1100, 0, 1100000])

plt.show()