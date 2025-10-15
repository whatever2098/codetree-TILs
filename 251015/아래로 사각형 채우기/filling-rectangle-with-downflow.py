import sys
input = sys.stdin.readline

n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

num = 1
for j in range(n):
    for i in range(n):
        board[i][j] = num
        num += 1

for i in range(n):
    for j in range(n):
        print(board[i][j], end=" ")
    print()    

        

        
