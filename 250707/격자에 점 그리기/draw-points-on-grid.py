N, M = map(int, input().split())

#ex_spots = list(map(int, input().split()))

matrix = [[0] * N for _ in range(N)] #2차원 행렬
'''올바른 리스트 컴프리헨션 사용: [표현식 for 변수 in 반복가능객체]
[0 * N] => X   리스트 반복이 아니고 산술 연산이다.'''

# 2) M개의 점을 입력받아, 순서(1~M)대로 matrix에 기록
for k in range(1, M+1):
    r, c = map(int, input().split())
    matrix[r-1][c-1] = k

# 3) 완성된 행렬 출력
for row in matrix:
    print(' '.join(map(str, row)))
