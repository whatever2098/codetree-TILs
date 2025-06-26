def to_base(n: int, base: int) -> str:
    """
    n을 base 진법 문자열로 반환한다.
    base는 4 또는 8.
    0이면 "0"을, 양수면 반복 나눗셈으로 구한다.
    """
    if n == 0:
        return "0"

    digits = []
    # 0~base-1 결과를 문자로 바꿀 테이블
    # (여기서는 base<=10 이므로 "0"~"9"만 쓴다)
    table = "0123456789"

    # 1) n이 0이 될 때까지 반복
    while n > 0:
        n, rem = divmod(n, base)
        # rem은 0..base-1 범위
        digits.append(table[rem])
        # 예: n=123, base=4 → rem=3, n=30 → digits=['3'], 다음

    # 2) 나머지들을 역순으로 읽어야 올바른 자릿수 순서
    return "".join(reversed(digits))


def main():
    # 입력: 정수 N, 목표 진법 B (4 또는 8)
    N, B = map(int, input().split())

    # 진법 변환
    result = to_base(N, B)

    # 출력
    print(result)


if __name__ == "__main__":
    main()


