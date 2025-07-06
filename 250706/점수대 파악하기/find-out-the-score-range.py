input_arr = list(map(int, input().split()))

division = [0] * 10 #0 부터 시작  1~10

for score in input_arr:
    if score == 0 or score < 10:
        break
    
    if score >= len(division):                                                                                  score = len(division) - 1

    division[score] += 1

for i in range(10):
    print(f"{i * 10} - {division[i]}")