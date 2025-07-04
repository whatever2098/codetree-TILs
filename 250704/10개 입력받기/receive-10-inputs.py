import sys

# 1) stdin 전체를 읽어서 공백 단위로 분리
tokens = sys.stdin.read().split()

arr = []
total = 0
count = 0
# 2) 토큰을 순회하며 최대 10개 또는 0 등장 시 중단
for tok in tokens:
    if len(arr) >= 10:
        break
    x = int(tok)
    if x == 0:
        break
    arr.append(x)
    total += x
    count += 1

if count > 0:
    avg = total / count
    print(f"{total} {avg:.1f}")
else:
    print(" 0 0.0")
