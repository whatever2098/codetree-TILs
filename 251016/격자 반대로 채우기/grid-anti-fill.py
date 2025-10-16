import sys
input = sys.stdin.readline

n = int(input())

board = [[0] * n for _ in range(n)]
num = 1

# 오른쪽 끝 열(n-1)부터 왼쪽(0)으로 진행
for offset, j in enumerate(range(n - 1, -1, -1)):
    if offset % 2 == 0:           # 오른쪽에서 1,3,5...번째 열: 아래 -> 위
        for i in range(n - 1, -1, -1):
            board[i][j] = num
            num += 1
    else:                         # 2,4,6...번째 열: 위 -> 아래
        for i in range(n):
            board[i][j] = num
            num += 1

# 출력
for row in board:
    print(*row)