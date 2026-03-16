class SinhVien:
    count = 0  # biến class để đếm số đối tượng

    def __init__(self, diem):
        self.diem = diem
        SinhVien.count += 1  # tăng mỗi khi tạo đối tượng

    @classmethod
    def dem_so_luong(cls):
        return cls.count


# Tạo các đối tượng SinhVien
sv1 = SinhVien(8)
sv2 = SinhVien(7)
sv3 = SinhVien(9)

# In số lượng sinh viên đã tạo
print("Số đối tượng SinhVien đã tạo:", SinhVien.dem_so_luong())