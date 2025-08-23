import sys
input = sys.stdin.readline

arr = [0] * 10
a, b = map(int, input().split())
arr[0] = a; arr[1] = b

for i in range(2, 10):
    arr[i] = (arr[i - 1] + arr[i - 2]) % 10
    
print(*arr)
