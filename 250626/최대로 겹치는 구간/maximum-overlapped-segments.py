'''n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
#segments = [(, )(, )(, )]...

blanks = [0 for _ in range(n)]

for segment in segments:
    segment1, segment2 = segment

    for i in range(segment1 - 1, segment2):
        blanks[i] += 1
            

blanks.sort(reverse = True)
print(blanks[1])'''

n = int(input())
events = []

for _ in range(n):
    a, b = map(int, input().split())
    events.append((a,  1))
    events.append((b+1, -1))

# 정렬: 좌표 오름차순, 동일 좌표면 +1 먼저
events.sort(key=lambda x: (x[0], -x[1]))

current = best = 0
for _, delta in events:
    current += delta
    if current > best:
        best = current

print(best)

