n = int(input())

nums = list(map(int, input().split()))
counts = [0] * n
#counts = [0 for i in range(10)]

for i in range(n):
    if nums[i] == i:
        counts[i] += 1
for i in range(n):
    print(counts[i])