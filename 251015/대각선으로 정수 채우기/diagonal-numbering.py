n, m = map(int, input().split())

board = [[0] * m for _ in range(n)]
num = 1

for start_row in range(n):
    i, j = start_row, 0
    while i >= 0 and j < m:
        board[i][j] = num
        num += 1
        i -= 1
        j += 1

for start_col in range(1, m):
    i, j = n - 1, start_col
    while i >= 0 and j < m:
        board[i][j] num
        num += 1
        i -= 1
        j += 1

for row in board:
    print(*row)