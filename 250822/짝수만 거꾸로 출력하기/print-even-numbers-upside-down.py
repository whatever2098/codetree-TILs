import sys
input = sys.stdin.readline

nums = int(input())
temp_ls = list(map(int, input().split()))

sequence_list = []

for e in (temp_ls):
    if e % 2 == 0:
        sequence_list.append(e)


#print(" ".join(map(str, sequence_list[::-1])))
print(*sequence_list[::-1]) #=unpack 연산자 사용

