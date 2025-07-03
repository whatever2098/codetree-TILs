arr = []
total = 0

# 1) 입력 받기 (최대 10개, 0 입력 시 중단)
for _ in range(10):
    for tok in input().split():
        x = int(tok)
        if x == 0:
            break
        arr.append(x)
        total += x
    else:
        # inner for가 0 없이 끝났으면 다음 반복으로
        continue
    # inner for에서 break 발생(=0 입력)하면 완전 탈출
    break

# 2) 합계와 평균 계산
count = len(arr)
if count > 0:
    avg = total / count
    # 3) total 과 평균(.1f) 출력
    # 예: 20 5.0
    print(f"{total} {avg:.1f}")
else:
    # 입력된 값이 없다면 0 0.0 출력 (필요에 따라 변경)
    print("0 0.0")
