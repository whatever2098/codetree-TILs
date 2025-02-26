user2_id, user2_level = input().split()

class User:
    def __init__(self, id, level):
        self.id = id
        self.level = level

user1 = User("codetree", str(10))
user2 = User(user2_id, user2_level)

print("user " + user1.id + " lv " + user1.level)
print("user " + user2.id + " lv " + user2.level)