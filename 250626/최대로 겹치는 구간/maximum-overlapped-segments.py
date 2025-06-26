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

# 1) 세그먼트 개수 n
n = int(input().strip())

# 2) 이벤트 리스트 만들기
#    구간 [a, b]가 포함 구간이라면
#    (a, +1) → 겹침 시작
#    (b+1, -1) → b까지 포함했으니 그 다음부터 빠짐
events = []
for _ in range(n):
    a, b = map(int, input().split())
    events.append((a,  1))
    events.append((b+1, -1))

# 3) 좌표순으로 정렬하되,
#    동일 좌표면 “+1”이 먼저 처리되도록
events.sort(key=lambda ev: (ev[0], -ev[1]))

# 4) 한 줄씩 스윕하며 최대값 계산
current = 0
best = 0
for coord, delta in events:
    current += delta
    if current > best:
        best = current

# 5) 정답 출력
print(best)

