'''문제: N개의 정수 중 최솟값과 최댓값을 구하는 프로그램'''

import sys
input = sys.stdin.readline

def solve():
  n = int(input())
  nums = list(map(int,input().split()))       #list == 파이썬 내장형과 헷갈리게 된다. 다른 이름 필요.

  mn = min(nums)
  mx = max(nums)

  print(mn, mx)

if __name__ == "__main__":
    solve()