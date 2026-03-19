while True:
    print("\n--- MENU ---")
    print("1. Bài 9 (OOP)")
    print("2. Bài 10 (Bubble Sort)")
    print("0. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        print("Chạy Bài 9...")
        p = Person("Test", 25)
        print(p)

    elif choice == "2":
        print("Chạy Bài 10...")
        arr = ["a", "abcd", "abc", "ab", "abcdef"]
        arr.sort(key=len, reverse=True)
        print(arr)

    elif choice == "0":
        print("Thoát chương trình!")
        break

    else:
        print("Lựa chọn không hợp lệ!")