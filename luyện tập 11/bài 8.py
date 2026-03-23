# Chương trình lấy tên tuổi và điểm trung bình của sinh viên

def main():
    name = get_name()
    age = get_age()
    score = get_score()
    print(f"{name} from {age} from {score}")

def get_name():
    return input("Name; ")

def get_age():
    return input("Age; ")

def get_score():
    return input("Score; ")

if __name__ == "__main__":
    main()

