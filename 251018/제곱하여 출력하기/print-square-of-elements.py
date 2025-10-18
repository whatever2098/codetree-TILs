import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

for elem in lst:
    print(elem ** 2, end=" ")
print()