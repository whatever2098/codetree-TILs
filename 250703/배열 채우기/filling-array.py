arr = []

# 최대 10개, 중간에 0이 나오면 즉시 중단
while len(arr) < 10:
    # 한 줄에서 공백으로 구분된 여러 숫자를 리스트로 읽어들임
    tokens = input().split()
    for tok in tokens:
        x = int(tok)
        if x == 0:
            # 0이 나오면 이중 루프 탈출
            break_flag = True
            break
        arr.append(x)
        if len(arr) == 10:
            break
    else:
        # for-else: break가 걸리지 않았으면 while 계속
        continue
    # for에서 break(0 감지)했으면 while도 탈출
    break

# 입력된 값들을 역순으로 출력
for v in reversed(arr):
    print(v, end=" ")
