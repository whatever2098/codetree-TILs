import sys
input = sys.stdin.readline

integers = list(map(int, input().split()))

cnt_even = 0
total_even = 0

for i in range(10):
    if integers[i] != 0:
        if integers[i] % 2 == 0:
            cnt_even += 1
            total_even += integers[i]
    else: break
print(cnt_even, total_even)
    