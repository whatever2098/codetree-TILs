import sys
input = sys.stdin.readline

N, Q = input().split()
N = int(N)
Q = int(Q)
element = input().split() #list

instruction = ""
for _ in range(Q):
    if instruction == "1 a":
        print(element[a])
    elif instruction == "2 b":
        if b in element:
            print(element.index(b))
        else: print(0)
    elif instruction == "3 s e":
        for i in range(s-1, e):
            print(element[i] + " ")
    

