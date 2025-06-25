secret_code, meeting_point, time = input().split()
time = int(time)

class zzseven:
    def __init__ (self, secret_code, meeting_point, time):
        self.sc = secret_code
        self.mp = meeting_point
        self.time = time

member1 = zzseven("codetree", "L", 13)

print("secret code : " + member1.sc)
print("meeting point : " + member1.mp)
print("time : " + str(member1.time))