n = int(input())
nums = list(map(int, input().split()))

middles = list()
for i in range (n):
    if i % 2 == 0:
        middles.append(sorted(nums[:i+1])[i // 2])

print(" ".join(map(str, middles)))