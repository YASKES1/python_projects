import matplotlib.pyplot as plt
plt.style.available

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


#стилі
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

#поставити точку на графіку на координатах, задати колір градієнт
#cmap - мапа кольорів - функція градієнту в plotlib

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# задати назву для графіка кожної осей

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)

#задати розмір шрифту підписів
ax.tick_params(axis='both', which='major', labelsize=14)

#задати діпазон для кожної з осей
ax.axis([0, 1100, 0, 1100000])

plt.show()

#збереження діаграм
plt.savefig('square_plot.png', bbox_inces='tight')