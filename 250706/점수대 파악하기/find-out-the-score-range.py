input_arr = list(map(int, input().split()))

# 2) 0~9→인덱스0, 10~19→인덱스1, …, 90~99→인덱스9, 100→인덱스10
division = [0] * 11  

for score in input_arr:
    if score == 0:      # 0이면 종료
        break
    if score < 0:       # 음수 무시(필요시)
        continue

    idx = score // 10
    if idx > 10:        # 100점 초과는 100점 버킷에 몰기(선택)
        idx = 10
    division[idx] += 1

# 3) 100, 90, …, 10 점 순으로 출력
for i in range(10, 0, -1):
    print(f"{i*10} - {division[i]}")
