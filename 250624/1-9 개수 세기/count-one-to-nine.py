n = int(input())
k = list(map(int, input().split()))

counts = [0 for _ in range(9)]

#등장 횟수 누적
for value in k:
    counts[value - 1] += 1

for i in range(1, 10):
    print(counts[i-1])