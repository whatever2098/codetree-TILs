count = 1 #시작일을 포함

m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


while not (m1 == m2 and d1 == d2):
    d1 += 1
    count += 1

    if d1 > num_of_days[m1]:
        m1 += 1
        d1 = 1


print(count)