n, k = map(int, input().split())

arrs = [0 for i in range( n + 1 )]

for _ in range(k):
   a, b = map(int, input().split())
   
   if a > 0 and b > 0:
    l, r = min(a, b), max(a, b)
    for i in range(l, r + 1):
        arrs[i] += 1

print(max(arrs))