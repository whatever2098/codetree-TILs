n = int(input())

students = []
for _ in range(n):
    # 1) split 결과를 바로 언패킹
    name, s1, s2, s3 = input().split()
    # 2) 점수 문자열을 정수로 변환
    s1, s2, s3 = int(s1), int(s2), int(s3)

    # 3) students 리스트에 튜플로 추가
    students.append((name, s1, s2, s3))

# 4) 총점(국어+영어+수학) 기준 오름차순 정렬
students.sort(key=lambda x: x[1] + x[2] + x[3])

# 5) 언패킹해서 출력
for name, kor, eng, math in students:
    print(name, kor, eng, math)
