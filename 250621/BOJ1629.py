'''BOJ 1629번:곱셈
  a**n * a**n = a**2n
  1번 도미노가 쓰러진다. k번 도미노가 쓰러지면 K+1번 도미노도 쓰러진다
  1승을 계산할 수 있다. k승을 계산했으면 2k승과 2k+1승도 O(1)에 계산할 수 있다.
  <수학적 귀납법>''' #시간복잡도 O(log b)



ll(input().split())
def multiple(A, B, C):
  if C == 0:
    A % C == 0
  return multiple(A, B, A % C)