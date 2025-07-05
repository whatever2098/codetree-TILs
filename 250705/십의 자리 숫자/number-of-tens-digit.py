# 십의 자리 숫자를 셀 카운트 배열 (0~9)
counts = [0] * 10

# 입력값을 한 줄로 읽어서, 0이 나오기 전까지만 순회
nums = list(map(int, input().split()))
for num in nums:
    if num == 0:
        break        # 0 나오면 종료
    # 0~99 범위이므로 //10 한 값이 바로 “십의 자리 숫자”
    ten = num // 10
    counts[ten] += 1

# 1~9 십의 자리만 출력
for i in range(1, 10):
    print(f"{i} - {counts[i]}")

