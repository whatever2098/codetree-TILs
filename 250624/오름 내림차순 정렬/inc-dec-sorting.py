n = int(input())
nums = list(map(int, input().split()))

nums.sort()
for x in nums:
    print(x, end=" ")
nums.sort(reverse = True)
print()
for x in nums:
    print(x, end=" ")
