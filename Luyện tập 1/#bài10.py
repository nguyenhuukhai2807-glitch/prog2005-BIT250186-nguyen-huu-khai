from matplotlib import pyplot as plt

categories = ['Bia', 'Cocacola', 'Bưởi5Roi']
values = [14.5, 15.5, 18.0]

plt.pie(values, labels=categories)
plt.title("Pie Chart")
plt.show()