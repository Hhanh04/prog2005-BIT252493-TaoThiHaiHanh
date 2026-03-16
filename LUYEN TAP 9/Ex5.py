# Bài 5:
class User:
    def __init__(self, user_id):
        self._id = user_id

    @property
    def id(self):
        return self._id


def bai5():
    print("Bài 5: Lớp User với id read-only")
    user = User(12345)
    print(f"User ID: {user.id}")
    print("-" * 50)
