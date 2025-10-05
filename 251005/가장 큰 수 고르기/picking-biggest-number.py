import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

max_num = arr[0]

for i in range(1, 10):
    if arr[i] > max_num:
        max_num = arr[i]

print(max_num)