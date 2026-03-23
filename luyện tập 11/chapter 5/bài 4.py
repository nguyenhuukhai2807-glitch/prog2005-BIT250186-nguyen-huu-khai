import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
df = pd.read_csv('california_cities.csv')

# Sắp xếp theo diện tích giảm dần và lấy top 10
top10 = df.sort_values(by='area_total_km2', ascending=False).head(10)

# Vẽ biểu đồ cột ngang
plt.barh(top10['city'], top10['area_total_km2'])

# Đảo trục y để thành phố lớn nhất nằm trên
plt.gca().invert_yaxis()

# Tiêu đề và nhãn
plt.title('Top 10 thành phố lớn nhất California theo diện tích')
plt.xlabel('Diện tích (km²)')
plt.ylabel('Thành phố')

plt.show()