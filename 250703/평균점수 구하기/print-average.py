# 8개의 실수 점수를 한 줄씩 입력받아 리스트로 저장
scores = list(map(float, input().split()))

# 총합과 평균 계산
total = sum(scores)
average = total / 8

# 소수점 첫째 자리까지 출력
# 방법1: f-string
print(f"{average:.1f}")

# 방법2: format 함수
# print(format(average, ".1f"))
