#Nhập cân nặng (kg)
weight = float(input("Nhập cân nặng (kg): "))

#Nhập chiều cao (m)
height = float(input("Nhập chiều cao (m): "))

#Tính BMI
bmi = weight / (height * height)

#Hiển thị kết quả làm tròn 2 chữ số thập phân
print("BMI của bạn là:", round(bmi, 2))