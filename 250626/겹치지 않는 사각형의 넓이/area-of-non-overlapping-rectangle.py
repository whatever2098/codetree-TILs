def rect_area(x1, y1, x2, y2):
    """좌표 (x1,y1)–(x2,y2)로 정의된 축병렬 직사각형의 넓이."""
    return max(0, x2 - x1) * max(0, y2 - y1)

def overlap_area(a, b):
    """
    a, b 각각 (x1,y1,x2,y2) 튜플인 두 직사각형의 
    교집합 넓이를 반환.
    """
    x1 = max(a[0], b[0])
    y1 = max(a[1], b[1])
    x2 = min(a[2], b[2])
    y2 = min(a[3], b[3])
    # 겹치지 않으면 음수가 나오는데, 그땐 넓이를 0으로
    return rect_area(x1, y1, x2, y2)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    # A
    ax1, ay1, ax2, ay2 = map(int, input().split())
    # B
    bx1, by1, bx2, by2 = map(int, input().split())
    # M (덮개)
    mx1, my1, mx2, my2 = map(int, input().split())

    A = (ax1, ay1, ax2, ay2)
    B = (bx1, by1, bx2, by2)
    M = (mx1, my1, mx2, my2)

    # 1) 전체 넓이
    area_A = rect_area(*A)
    area_B = rect_area(*B)

    # 2) 겹친 넓이
    ov_A = overlap_area(A, M)
    ov_B = overlap_area(B, M)

    # 3) A, B에서 M에 덮이지 않은 순수 넓이 합
    result = (area_A - ov_A) + (area_B - ov_B)
    print(result)


