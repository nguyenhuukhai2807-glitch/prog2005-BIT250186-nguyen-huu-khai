class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

    def display(self):
        print(f"Sinh viên {self.ten} có điểm là { self.diem}")


#Khởi tạo đối tượng
sv1 = Student("A", 10)
sv2 = Student("B", 8)

