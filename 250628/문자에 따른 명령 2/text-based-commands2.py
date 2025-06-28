# 입력
commands = input().strip()  # 예: "FFRFLF..."

# 방향 벡터 (북, 동, 남, 서)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 시작 위치와 방향 인덱스 (0=북)
x, y = 0, 0
dir_idx = 0

# 명령 처리
for cmd in commands:
    if cmd == 'L':
        dir_idx = (dir_idx - 1 + 4) % 4
    elif cmd == 'R':
        dir_idx = (dir_idx + 1) % 4
    elif cmd == 'F':
        x += dx[dir_idx]
        y += dy[dir_idx]
    # 그 외 문자는 무시

# 결과 출력
print(x, y)