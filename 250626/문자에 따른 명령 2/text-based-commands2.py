dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cmds = list(input().strip())

x = 0
y = 0
dir_num = 0

for cmd in cmds:
    if cmd == 'F':
        x += dx[dir_num]
        y += dy[dir_num]
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        dir_num = (dir_num - 1) % 4

print(x, y)



