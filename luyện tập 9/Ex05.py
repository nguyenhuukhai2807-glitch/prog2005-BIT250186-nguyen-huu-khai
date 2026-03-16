class User:
    def __init__(self, user_id):
        self._id = user_id   # thuộc tính ẩn

    @property
    def id(self):
        return self._id      # chỉ cho phép đọc

# Tạo đối tượng
user = User(101)

#Đọc id
print("User ID:", user.id)

#Thử thay đổi id (sẽ lỗi)
user.id = 200


