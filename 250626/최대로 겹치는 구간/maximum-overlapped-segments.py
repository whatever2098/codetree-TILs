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
n = int(input())

# 2) (a,b) 세그먼트 리스트 읽기
segments = [tuple(map(int, input().split())) for _ in range(n)]

# 3) 가장 멀리 뻗은 끝 점을 찾아서
max_coord = max(b for _, b in segments)

# 4) 그 끝 점까지 담을 수 있게 blanks 초기화
#    (1-based 입력을 0-based [0..max_coord-1] 로 다룰 거라 길이를 max_coord로)
blanks = [0] * max_coord

# 5) 각 세그먼트 [a..b] (포함) 구간에 대해
#    1-based→0-based 변환: range(a-1, b)
for a, b in segments:
    for i in range(a - 1, b):
        blanks[i] += 1

blanks.sort(reverse=True)
print(blanks[0])
