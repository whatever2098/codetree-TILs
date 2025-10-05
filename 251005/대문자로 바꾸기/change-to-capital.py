import sys
input = sys.stdin.readline

arr = [list(input().split()) for _ in range(5)]

for i in range(5):
    for j in range(3):
        arr[i][j] = arr[i][j].upper()

for i in range(5):
    print(*arr[i]) 
