class Person:
    count = 0  # class variable

    def __init__(self, name, age):
        # Cách 1: validate trực tiếp
        if age < 0:
            raise ValueError("Tuổi không hợp lệ!")

        self._name = name
        self._age = age
        Person.count += 1

    # Getter
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    # Setter
    def set_age(self, age):
        # Cách 2: validate trong setter
        if age < 0:
            raise ValueError("Tuổi phải >= 0")
        self._age = age

    # __str__
    def __str__(self):
        return f"Person(name={self._name}, age={self._age})"

    # Phương thức đối tượng
    def greet(self):
        return f"Xin chào, tôi là {self._name}"

    # Class method
    @classmethod
    def get_count(cls):
        return cls.count

    # Static method
    @staticmethod
    def is_adult(age):
        return age >= 18

    # Nạp chồng toán tử ==
    def __eq__(self, other):
        return self._name == other._name and self._age == other._age


# Class kế thừa
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        if grade < 0:
            raise ValueError("Điểm không hợp lệ!")
        self._grade = grade

    def __str__(self):
        return f"Student(name={self._name}, age={self._age}, grade={self._grade})"

    # override method
    def greet(self):
        return f"Xin chào, tôi là sinh viên {self._name}"


# ===== TEST =====
p1 = Person("An", 20)
p2 = Person("An", 20)
s1 = Student("Bình", 18, 9.0)

print(p1)
print(p1.greet())
print("Số person:", Person.get_count())
print("Có phải người lớn:", Person.is_adult(20))

print("So sánh p1 == p2:", p1 == p2)

print(s1)
print(s1.greet())