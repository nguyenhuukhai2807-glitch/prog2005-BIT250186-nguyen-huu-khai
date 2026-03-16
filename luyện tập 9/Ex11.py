class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  # gọi constructor của lớp cha

    def sound(self):
        print("Woof Woof!")  # ghi đè phương thức


Dog = Dog("độ")
print("têm:", Dog.name)
Dog.sound()


