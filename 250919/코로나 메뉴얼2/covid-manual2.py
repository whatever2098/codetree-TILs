import sys
input = sys.stdin.readline


state = [0, 0, 0, 0]

for _ in range(3):
    symp, temp = input().split()
    t = float(temp)
    if symp == "N" and t < 37:
        state[3] += 1 #D
    elif symp == "Y" and t < 37:
        state[2] += 1 #C
    elif symp == "N" and t >= 37:
        state[1] += 1 #B
    elif symp == "Y" and t >= 37:
        state[0] += 1 #A
        

print(*state, end='')
if state[0] >= 2:
   print(" E")
else:
    print()