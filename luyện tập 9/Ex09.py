class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    def __eq__(self, other):
        return self.diem == other
