n, m = map(int, input().split())

board = [[0] * m for _ in range(n)]  #n, m이 바뀌었어

num = 0
for j in range(m):
    if j % 2 == 0:
        for i in range(n):
            board[i][j] = num
            num += 1
    else:
        for i in range(n - 1, -1, -1):
            board[i][j] = num
            num += 1

for row in board:
    for elem in row:
        print(elem, end=" ")
    print()