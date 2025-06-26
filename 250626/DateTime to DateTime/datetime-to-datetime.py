def main():
    A, B, C = map(int, input().split())
    # 기준 시각: 2011-11-11 11:11
    # 목표 시각: 2011-11-A  B:   C

    # 두 시각을 “11일 11:11”부터 경과된 분으로 바꿔 빼면 차이가 나옵니다.
    base = 11 * 24 * 60 + 11 * 60 + 11
    target = A  * 24 * 60 +    B * 60 +    C
    diff = target - base

    # 목표가 기준보다 이전이면 -1
    if diff < 0:
        print(-1)
    else:
        print(diff)

if __name__ == "__main__":
    main()
