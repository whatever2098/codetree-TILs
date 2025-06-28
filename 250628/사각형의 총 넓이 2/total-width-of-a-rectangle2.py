n = int(input())
rects = [tuple(map(int, input().split())) for _ in range(n)]

OFFSET = 100
SIZE = 2 * OFFSET + 1     # -100…100  → 0…200 인덱스
grid = [[0] * SIZE for _ in range(SIZE)]

# 각 사각형마다 덮는 칸(cell)을 표시
for a, b, c, d in rects:
    x1 = a + OFFSET
    y1 = b + OFFSET
    x2 = c + OFFSET
    y2 = d + OFFSET
    # x ∈ [x1, x2), y ∈ [y1, y2)
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] += 1

# grid[x][y] > 0 인 칸의 개수 = 합집합 넓이
area = 0
for row in grid:
    for cell in row:
        if cell > 0:
            area += 1

print(area)

