n, k = map(int, input().split())

blocks = [0 for _ in range(n + 1)]

for _ in range(k):
  a, b = map(int, input().split())
  for i in range(a, b + 1):
    blocks[i] += 1
    
blocks.sort(reverse = True)
print(blocks[1])