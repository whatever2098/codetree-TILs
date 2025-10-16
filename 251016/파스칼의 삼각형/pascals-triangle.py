import sys
input = sys.stdin.readline

n = int(input())

board = [[1] * n for _ in range(n)]

for i in range(2, n):
    for j in range(1, i):
        board[i][j] = board[i - 1][j - 1] + board[i - 1][j]

for i in range(n):
    print(*board[i][:i + 1])