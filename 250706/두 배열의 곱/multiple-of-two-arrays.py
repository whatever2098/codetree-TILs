# 1) 두 행렬 입력
arr1 = [ list(map(int, input().split())) for _ in range(3) ]
_ = input()    # 이 한 줄이 공백(혹은 완전 빈 문자열)이면 그냥 넘어갑니다.
arr2 = [ list(map(int, input().split())) for _ in range(3) ]

# 2) 결과용 3×3 제로 행렬 미리 생성
result = [ [0]*3 for _ in range(3) ]

# 3) 대응 원소 곱 계산
for i in range(3):
    for j in range(3):
        result[i][j] = arr1[i][j] * arr2[i][j]

# 4) 출력 (각 행을 한 줄에)
for row in result:
    print(*row)
