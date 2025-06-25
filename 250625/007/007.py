class zzseven:
    def __init__(self, secret_code, meeting_point, time):
        self.sc = secret_code
        self.mp = meeting_point
        self.time = time

# 첫 줄 입력을 한 번만 읽어서 초기화
secret_code, meeting_point, time_str = input().split()
time_val = int(time_str)
memberi = zzseven(secret_code, meeting_point, time_val)

while True:
    line = input().strip()
    # 빈 줄이 들어오면 반복 종료
    if not line:
        break

    # 새로 들어온 세 값을 파싱
    secret_code, meeting_point, time_str = line.split()
    time_val = int(time_str)

    # 멤버 속성 업데이트
    memberi.sc = secret_code
    memberi.mp = meeting_point
    memberi.time = time_val

    # 업데이트된 상태 출력
    print("secret code :", memberi.sc)
    print("meeting point :", memberi.mp)
    print("time :", memberi.time)
