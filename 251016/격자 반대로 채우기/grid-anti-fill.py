import sys
input = sys.stdin.readline

n = int(input())

board = [[0] * n for _ in range(n)]
num = 1

for j in range(n):  # 열(column) 기준 반복
    if j % 2 == 0:  # 짝수열이면 위 → 아래
        for i in range(n):
            board[i][j] = num
            num += 1
    else:           # 홀수열이면 아래 → 위
        for i in range(n - 1, -1, -1):
            board[i][j] = num
            num += 1

# 출력
for row in board:
    print(*row)
