# 1) arr[0]은 '1'의 개수, arr[1]은 '2'의 개수, …, arr[5]는 '6'의 개수
arr = [0] * 6

# 2) 입력받아서 바로 순회하며 세기
elem = list(map(int, input().split()))
for e in elem:
    if 1 <= e <= 6:
        arr[e-1] += 1

# 3) 출력
for i, cnt in enumerate(arr, start=1):
    print(f"{i} - {cnt}")

        
    