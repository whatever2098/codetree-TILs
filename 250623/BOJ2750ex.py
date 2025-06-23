import sys
input = sys.stdin.readline

n = int(input().strip()) #줄바꿈 제거 후 정수 변환

min_values = []
for _ in range(n):
  numbers = map(int, input().split())  #한 줄기의 정수들
  min_values.append(min(numbers))
  
for m in min_values:
  print(m)