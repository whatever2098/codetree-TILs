import sys
input = sys.stdin.readline

n = int(input().strip())
arr = [1, n]

while True:
    nxt = arr[-1] + arr[-2]
    arr.append(nxt)
    if nxt > 100:
        break

print(*arr)
      