'''n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

n, k = map(int, input().split())

blocks = [0 for _ in range(n + 1)]

for a, b in range(k):
  if a >= b or a <= b:
    blocks[a:b + 1:-1] += 1
    
blocks.sort(reverse = True)
print(blocks[1])'''

'''n, k = tuple(map(int, input().split()))
segments = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

blocks = [0] * (n + 1)

# 블럭을 특정 구간에 쌓아줍니다.
for a, b in segments:
    for i in range(a, b + 1):
        blocks[i] += 1

# 최댓값을 구합니다.
max_num = max(blocks)
print(max_num)'''


n, k = map(int, input().split())

blocks = [0 for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a - 1, b):  #여기를 알 수 없음
        blocks[i] += 1


blocks.sort(reverse = True)
print(blocks[0])