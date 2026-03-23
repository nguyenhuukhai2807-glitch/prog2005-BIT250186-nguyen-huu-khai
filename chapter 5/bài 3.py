import matplotlib.pyplot as plt

# Dữ liệu
labels = ['A', 'B', 'C', 'D', 'E']
sizes = [30, 25, 15, 20, 10]

# Vẽ biểu đồ tròn
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Tiêu đề
plt.title('Tỷ lệ doanh số các sản phẩm')

plt.show()