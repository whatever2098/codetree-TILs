import sys
input = sys.stdin.readline

# 2x4 배열 선언
arr = [list(map(int, input().split())) for _ in range(2)]

# 각 행 평균 출력 (2행)
for i in range(2):
    s = 0
    for j in range(4):
        s += arr[i][j]
    print(s / 4, end=" ")
print()

# 각 열 평균 출력 (4열)
for j in range(4):
    s = 0
    for i in range(2):
        s += arr[i][j]
    print(s / 2, end=" ")
print()

# 전체 평균
total = 0
for i in range(2):
    for j in range(4):
        total += arr[i][j]

print(total / 8)
