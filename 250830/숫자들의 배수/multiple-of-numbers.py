import sys
input = sys.stdin.readline

n = int(input())   # 1 이상 10 이하의 정수 입력
count = 0          # 5의 배수가 출력된 횟수
i = 1              # 배수를 만들기 위한 곱

while True:
    multiple = n * i
    print(multiple, end=" ")   # 한 줄에 공백으로 출력

    if multiple % 5 == 0:
        count += 1
        if count == 2:   # 5의 배수가 2번 나오면 종료
            break

    i += 1