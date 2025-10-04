import sys
input = sys.stdin.readline

# 첫 줄: N(정수)와 M(문자열)
first = input().split()
N = int(first[0])
M = first[1]

arr = input().split()

ans = arr.count(M)
print(ans)
