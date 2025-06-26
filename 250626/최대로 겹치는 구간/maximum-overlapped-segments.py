n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
#segments = [(, )(, )(, )]...

blanks = [0 for _ in range(n)]

for segment in segments:
    segment1, segment2 = segment

    for i in range(segment1 - 1, segment2):
        blanks[i] += 1
            

blanks.sort(reverse = True)
print(blanks[1])