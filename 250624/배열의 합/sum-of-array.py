
total = 0

for i in range(4):
    arr_temp = list(map(int, input().split()))
    for j in range(4):
        total += arr_temp[j]
    print(total)
    total = 0