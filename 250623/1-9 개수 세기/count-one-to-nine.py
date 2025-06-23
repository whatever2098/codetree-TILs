n = int(input())

nums = list(map(int, input().split()))
counts = [0 for _ in range(10)]

for i in range(n):
    if nums[i] == i:
        counts[i] += 1
for i in range(9):
    print(counts[i])