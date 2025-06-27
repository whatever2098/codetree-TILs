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





'''import sys

def max_overlapping_segments(segments):
    """
    segments: [(x1, x2), ...] 형태의 리스트. 각 선분은 x1 < x2를 만족.
    반환값: 어떤 구간에서 가장 많이 겹치는 선분의 개수 (int)
    """
    # 1) 스위프 라인 이벤트 생성
    #    각 선분 (x1, x2) 에 대해
    #      (x1, +1) → 이 좌표부터 겹침 개수 +1
    #      (x2, -1) → 이 좌표부터 겹침 개수 -1
    events = []
    for x1, x2 in segments:
        events.append((x1, +1))
        events.append((x2, -1))

    # 2) 이벤트 정렬
    #    첫째 키: x 좌표 오름차순
    #    둘째 키: delta 값 오름차순  → 같은 x에서 -1이 +1보다 먼저
    #    → 끝점에서 딱 맞닿는 경우를 겹치지 않는 것으로 처리
    events.sort(key=lambda e: (e[0], e[1]))

    # 3) 한 번 스캔하며 최대값 추적
    current = 0  # 지금 스캔한 지점(바로 오른쪽)에 겹쳐 있는 선분 수
    best = 0     # 지금까지 본 최고 겹침 수

    for x, delta in events:
        current += delta     # 이벤트에 따라 +1 또는 -1
        if current > best:
            best = current   # 새로 최대치 갱신

    return best

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    segments = []
    for _ in range(N):
        x1, x2 = map(int, input().split())
        segments.append((x1, x2))
    print(max_overlapping_segments(segments))

if __name__ == "__main__":
    main()
'''




n = int(input())

# x1+OFFSET, x2+OFFSET 의 최대값이 200이므로
# 0부터 200까지 총 201칸을 확보해야 안전합니다.
blocks = [0 for _ in range(2 * 100 + 1)]

for _ in range(n):
    x1, x2 = map(int, input(). split())
    x1 += 100
    x2 += 100
   # 슬라이스랑 정수는 +=계산 못 함 blocks[x1:x2] += 1
    for i in range(x1, x2):
        blocks[i] += 1

print(max(blocks))
