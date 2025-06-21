def reverse(my_list):          # ① 함수 정의: 리스트를 뒤집어 반환
    if len(my_list) <= 1:      # ② 재귀의 종료(기저) 조건 → 길이가 0 또는 1이면 그대로 반환
        return my_list
    # ③ 재귀 부분:
    #    - my_list[-1:]  : 마지막 원소를 '리스트' 형태로 추출
    #    - my_list[:-1] : 마지막 원소를 뺀 나머지 부분
    #    - 두 리스트를 + 연산자로 이어 붙이면 새로운 리스트가 만들어짐
    return my_list[-1:] + reverse(my_list[:-1])

print(reverse([5, 2, 7, 1, 4]))  # ④ 실행 & 결과 확인 → [4, 1, 7, 2, 5]
