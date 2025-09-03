import sys
input = sys.stdin.readline

a1, a2 = map(int, input().split())

def fib(a1: int, a2: int, n: int) -> list[int]:
    res = [0] * (n + 1)
    res[0] = a1;
    res[1] = a2;

    for i in range(2, n + 1):
        res[i] = res[i - 1] + 2 * res[i - 2]
    
    return res


print(*fib(a1, a2 , 9 ))