import sys
input = sys.stdin.readline

arr_2d = [list(map(int, input().split())) for _ in range(2)]

#가로평균 2개
avg_row = []
for i in range(2):
    total = 0
    for j in range(4):
        total += arr_2d[i][j]
    avg_row.append(total / 4)

print(*[f"{x:.1f}" for x in avg_row])

avg_col = []
for j in range(4):
    total = 0
    for i in range(2):
        total += arr_2d[i][j]
    avg_col.append(total / 2)

print(*[f"{x:.1f}" for x in avg_col])

total_sum = sum(sum(row) for row in arr_2d)
avg_whole = total_sum / (2 * 4)
print(f"{avg_whole:.1f}")




