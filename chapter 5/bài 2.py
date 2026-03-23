import numpy as np
import matplotlib.pyplot as plt

# Dữ liệu
x = np.linspace(-10, 10, 100)
y1 = x**2
y2 = x**3

# Vẽ đồ thị
plt.plot(x, y1, color='blue', label='y = x^2')
plt.plot(x, y2, color='red', label='y = x^3')

# Thêm chú thích
plt.legend()

# Tiêu đề
plt.title('Đồ thị y = x^2 và y = x^3')

plt.show()