n = int(input())
nums = list(map(int, input().split()))

nums.sort()

max_num = 0
for i in range (n):
    result = nums[i] + nums[2 * n - 1 - i]
    if max_num < result:
        max_num = result

print(max_num)