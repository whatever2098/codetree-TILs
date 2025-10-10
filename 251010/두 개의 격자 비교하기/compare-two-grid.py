import sys
input = sys.stdin.readline

N, M = map(int, input().split())
first_grid = [[0] * (M + 1) for _ in range(N + 1)]
second_grid = [[0] * (M + 1) for _ in range(N + 1)]

new_grid = [[0] * (M + 1) for _ in range(N + 1)]

def read_grid(N, M):
    grid = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        row = list(map(int, input().split()))
        for j in range(1, M + 1):
            grid[i][j] = row[j - 1]
    return grid

first_grid = read_grid(N, M)
second_grid = read_grid(N, M)

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if first_grid[i][j] != second_grid[i][j]:
            new_grid[i][j] = 1

for i in range(1, N + 1):
    print(*new_grid[i][1:])

