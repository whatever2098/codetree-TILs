n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

m = len(grid[0])

answer = 0
for i in range(n):
    # j 에서 j, j+1, j+2 세 칸을 더하므로 마지막 j는 m-3
    for j in range(m - 2):
        total = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        if total > answer:
            answer = total

print(answer)
