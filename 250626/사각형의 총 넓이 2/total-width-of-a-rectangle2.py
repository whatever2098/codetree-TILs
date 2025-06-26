def total_area(rects):
    # 좌표를 0…200 범위의 인덱스로 바꾸기 위해 +100 시프트
    OFFSET = 100
    SIZE = 200   # –100…100 사이의 1×1 칸은 가로 200칸, 세로 200칸

    # 그리드 초기화: False = 아직 안 덮임
    covered = [[False] * SIZE for _ in range(SIZE)]

    for x1, y1, x2, y2 in rects:
        # 각 직사각형이 차지하는 정수 x, y 구간 [x1, x2), [y1, y2)
        # 을 단위칸으로 순회하며 covered 표시
        for x in range(x1, x2):
            for y in range(y1, y2):
                covered[x + OFFSET][y + OFFSET] = True

    # 넓이 = True로 표시된 칸 개수
    area = sum(
        1
        for i in range(SIZE)
        for j in range(SIZE)
        if covered[i][j]
    )
    return area

# 입력 처리
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input().strip())
    rects = [tuple(map(int, input().split())) for _ in range(n)]
    print(total_area(rects))


