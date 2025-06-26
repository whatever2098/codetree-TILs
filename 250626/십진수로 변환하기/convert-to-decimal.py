#binary = list(map(int, input().split()))
s = input().strip()
binary = [int(ch) for ch in s]

num = 0

for bit in binary:  #index없이 바로 bit를 꺼내 쓰면 더 깔끔
    num = num * 2 + bit

print(num)
