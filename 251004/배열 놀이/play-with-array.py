import sys
input = sys.stdin.readline

# N, Q
N, Q = map(int, input().split())

# 배열 원소 N개
element = list(map(int, input().split()))

for _ in range(Q):
    parts = input().split()        # 예) ["1","a"] 또는 ["3","s","e"]
    t = parts[0]

    if t == '1':
        a = int(parts[1])
        print(element[a - 1])      # 1-based → 0-based

    elif t == '2':
        b = int(parts[1])
        # 가장 작은 인덱스(1-based). 없으면 0
        try:
            print(element.index(b) + 1)   # .index는 0-based, 없으면 ValueError
        except ValueError:
            print(0)

    elif t == '3':
        s = int(parts[1])
        e = int(parts[2])
        # s번째부터 e번째까지 공백으로 구분하여 한 줄 출력
        print(' '.join(map(str, element[s - 1 : e])))
