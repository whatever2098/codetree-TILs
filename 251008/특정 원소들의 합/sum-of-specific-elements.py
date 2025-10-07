import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(4)]

colored = 0
for i in range(4):
    for j in range(4):
        if j <= i:          # 왼쪽 아래 삼각형(대각선 포함)
            colored += arr[i][j]

print(colored)

