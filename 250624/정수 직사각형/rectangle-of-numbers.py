n, m = map(int, input().split())
number = 1

for i in range(n):
    for j in range(m):
        print(number, end=" ")
        number += 1
    print()