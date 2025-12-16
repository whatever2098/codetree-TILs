import sys
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
arr =  [[0 for _ in range(M)] for _ in range(N)]                                #[[0] * M for _ in range(N)]
num = 1

for d in range(N + M - 1):
    for i in range(N):
        j = d - i
        if 0 <= j < M:
            arr[i][j] = num
            num += 1

for row in arr:
    print(*row)
