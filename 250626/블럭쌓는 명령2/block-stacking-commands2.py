n, k = map(int, input().split())

blocks = [0 for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a - 1, b):  #왜 a-1, b인지 궁금합니다
        blocks[i] += 1


blocks.sort(reverse = True)
print(blocks[1])