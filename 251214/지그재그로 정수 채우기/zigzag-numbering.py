import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = 0
answer = [[0] * M for _ in range(N)]
for j in range(M):
    if j % 2 == 0:
        for i in range(N):
            answer[i][j] = num
            num += 1
    else:
        for i in range(N - 1, -1, -1):
            answer[i][j] = num
            num += 1

for row in answer:
    print(*row)
    
