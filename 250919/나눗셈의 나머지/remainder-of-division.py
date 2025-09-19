import sys
input = sys.stdin.readline


A, B = map(int, input().split())

remainders = [0] * B

#for _ in range(A > 0):   A>0은 무한루프, A>1이 더 적합하다
while A > 1:             #(B >= 2 가정)
    #remain = A % B
    remainders[A % B] += 1
    A //= B


total = 0
for r in remainders:
    total += r * r

print(total)