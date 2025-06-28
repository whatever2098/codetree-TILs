n = int(input())
moves = [tuple(input().split()) for _ in range(n)] #[(dir, dist), (,)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx = [-1, 0, 0, 1]  #W,S,N,E
dy = [0, -1, 1, 0]

# dirs 배열에서 방향 문자를 인덱스로 바꿀 매핑
mapping = {"W":0, "S":1, "N":2, "E":3}

# 현재 위치
x, y = 0, 0

# 4) 각 이동 명령 처리
for dirc, dist in zip(dir, dist):
    # 방향 문자 → dx, dy 인덱스
    idx = mapping[dirc]
    # 이동 후 좌표 계산
    nx = x + dx[idx] * dist
    ny = y + dy[idx] * dist
    # 한번에 갱신
    x, y = nx, ny

# 최종 위치 출력
print(x, y)