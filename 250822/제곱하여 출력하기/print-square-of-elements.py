import sys
input = sys.stdin.readline

n = int(input())
square = list(map(int, input().split()))

for e in square:
    e = e ** 2
for i in range(len(square)):
    square[i] = square[i] ** 2
    

print(" ".join(map(str, square)))
 