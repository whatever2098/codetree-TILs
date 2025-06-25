MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

min_codename = str()
min_score = 100
for i in range (MAX_N):
    if scores[i] < min_score:
        min_score = scores[i]
        min_codename = codenames[i]

print(min_codename, min_score)