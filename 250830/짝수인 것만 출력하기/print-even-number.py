import sys
input = sys.stdin.readline

latest = []

n = int(input())
nums = list(map(int, input().split()))


'''for num in nums:
    if num % 2 == 0:
        latest.append(num)'''

latest = [num for num in nums if num % 2 == 0]


print(*latest)