import sys
input = sys.stdin.readline

N1, N2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# N2가 N1보다 크면 연속 부분수열일 수 없음
if N2 > N1:
    print("No")
    sys.exit(0)

found = False
for i in range(N1 - N2 + 1):
    if A[i:i+N2] == B:
        found = True
        break

print("Yes" if found else "No")
