code, color, second = input().split()

class Bomb_Defusal:
    def __init__(self, code, color, second):
        self.code_ = code
        self.color_ = color
        self.second_ = second

bomb_defusal = Bomb_Defusal(code, color, second)

print("code :", bomb_defusal.code_)
print("color :", bomb_defusal.color_)
print("second :", bomb_defusal.second_)