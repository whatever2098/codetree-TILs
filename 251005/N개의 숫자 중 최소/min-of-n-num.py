n = int(input())
a = list(map(int, input().split()))

cnt_min = 0
min_num = a[0]

for i in range(1, n):
    if min_num > a[i]:
        min_num = a[i]

for i in range(1, n):
    if min_num == a[i]:
        cnt_min += 1

print(str(min_num) + " " + str(cnt_min))

