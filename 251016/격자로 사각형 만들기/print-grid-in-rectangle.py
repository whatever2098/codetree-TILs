import sys
input = sys.stdin.readline

n = int(input())

board = [[1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != 0 and j != 0:
            board[i][j] = board[i - 1][j] + board[i][j - 1] + board[i - 1][j - 1]


for elem in board:
    print(*elem)