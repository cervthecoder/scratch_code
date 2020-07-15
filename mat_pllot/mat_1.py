from matplotlib import pyplot as plt

dev_x = [i for i in range(25, 35)]

dev_y = [38000, 40000, 41000, 42500, 45000, 50000, 51000, 52000, 52250, 60000]
lin_y = [n for n in range(35000, 45000) if (n%1000)==0]

plt.plot(dev_x, dev_y, 'k--',label='All Devs')
plt.plot(dev_x, lin_y, 'b',label='Python')

plt.xlabel('Age')
plt.ylabel('Salary')


plt.title('median Salary (USD) by Age')

plt.legend() #it shows the legend

plt.show()

