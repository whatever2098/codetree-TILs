import sys
input = sys.stdin.readline

arr = []
arr = list(map(int, input().split()))

zero_idx = -1

for i in range(len(arr)):
    if arr[i] == 0:
        zero_idx = i
        for j in range(0, zero_idx):
            if arr[j] % 2 == 0:
                arr[j] = arr[j] // 2
            else:
                arr[j] = arr[j] + 3
        break

arr = arr[0 : zero_idx]
print(*arr)
