import sys
input = sys.stdin.readline

# 2행 4열 입력
arr = [list(map(int, input().split())) for _ in range(2)]

# 1) 각 행의 평균
row1 = sum(arr[0]) / 4
row2 = sum(arr[1]) / 4

# 2) 각 열의 평균
col_avgs = []
for j in range(4):
    col_avgs.append((arr[0][j] + arr[1][j]) / 2)

# 3) 전체 평균
total_avg = (sum(arr[0]) + sum(arr[1])) / 8

# 출력
print(f"{row1:.1f} {row2:.1f}")
print(f"{col_avgs[0]:.1f} {col_avgs[1]:.1f} {col_avgs[2]:.1f} {col_avgs[3]:.1f}")
print(f"{total_avg:.1f}")
