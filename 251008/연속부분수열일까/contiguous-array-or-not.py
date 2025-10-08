import sys
input = sys.stdin.readline

N1, N2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N1):
    success = True
    for j in range(N2):
        if i + j >= N1:
            success = False
            break
        if A[i + j] != B[j]:
            success = False
            break
    if success:
        print("Yes")
        sys.exit()

print("No")

