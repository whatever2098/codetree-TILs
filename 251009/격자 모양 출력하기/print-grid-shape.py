import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst_2d = [[0] * (N + 1) for _ in range(N + 1)]  #0으로 격자 채움

for _ in range(1, M + 1):
    r, c = map(int, input().split())
    lst_2d[r][c] = r * c


for i in range(1, N + 1):
    for j in range(1, N + 1):
        print(lst_2d[i][j], end = " ")   
    print()
