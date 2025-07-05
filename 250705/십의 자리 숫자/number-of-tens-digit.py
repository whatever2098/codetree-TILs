# 1) 구간 개수: 0–9, 10–19, …, 90–99 → 총 10개
counts = [0] * 10

# 2) 입력 받기
numbers = list(map(int, input().split()))

# 3) 각 숫자에 대해 적절한 버킷 계산 및 카운트
for num in numbers:
    if num <= 0:
        # 음수는 무시하거나 별도 처리
        continue
    bucket = num // 10          # 정수 나눗셈 → 0,1,2,…,9
    if bucket >= len(counts):
        # 100 이상인 수는 맨 마지막 구간으로 몰아넣기
        bucket = len(counts) - 1
    counts[bucket] += 1
'''# 4) 결과 출력
        continue
    bucket = num // 10          # 정수 나눗셈 → 0,1,2,…,9
    if bucket >= len(counts):
        # 100 이상인 수는 맨 마지막 구간으로 몰아넣기
        bucket = len(counts) - 1
    counts[bucket] += 1

# 4) 결과 출력
for idx, cnt in enumerate(counts):
    print(f"{idx\} - {cnt\}")'''



'''for idx, cnt in enumerate(counts):
    if idx == 0:
        continue        # idx 0(0~9 구간)은 건너뛴다
    print(f"{idx} - {cnt}")'''


# counts[1:] 로 1~9 구간만 뽑아내고,
# enumerate(..., start=1) 으로 idx가 1부터 시작하게 만든다
for idx, cnt in enumerate(counts[1:], start=1):
    print(f"{idx} - {cnt}")
