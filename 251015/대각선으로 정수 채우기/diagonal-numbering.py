n, m = map(int, input().split())

board = [[0] * m for _ in range(n)]
num = 1

for start_col in range(m):
    i, j = 0, start_col
    while i < n and j >= 0:
        board[i][j] = num
        num += 1
        i += 1
        j -= 1

for start_row in range(1, n):
    i, j = start_row, m - 1
    while i < n and j >= 0:
        board[i][j] = num
        num += 1
        i += 1
        j -= 1

for row in board:
    print(*row)