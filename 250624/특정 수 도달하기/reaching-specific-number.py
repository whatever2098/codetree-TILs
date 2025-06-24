'''total = 0        # 누적 합용
count = 0        # 더한 개수

# 입력을 정수 리스트로 변환
arr = list(map(int, input().split()))

# 배열을 돌면서 합이 250 이상이면 중단
for value in arr:
    total += value
    count += 1
    if total >= 250:
        break

# 결과 출력: 합(total)과 평균(round)
if count > 0:
    average = round(total / count, 1)
    print({total}, {average})'''





# 1. 입력 받기
nums = list(map(int, input().split()))  # 10개의 정수가 공백으로 들어온다고 가정

# 2. 합계와 개수 초기화
total = 0
count = 0

# 3. 처음 250 이상이 나올 때까지 더하기
for x in nums:
    if x >= 250:
        break
    total += x
    count += 1

# 4. 평균 계산 및 출력
#    count는 최소 1(문제 조건에서 첫 수가 250 미만이 보장됨)이므로 0 나누기 걱정 없음
avg = round(total / count, 1)
print(f"{total} {avg}")
