'''n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
#1.현재 아는 정보: (x,y),   입력: dir(+ dist)

if m ==1 and d>31:
    m+=1
    d=1
elif m == 2 and d > 28:
    m += 1
    d = 1
    ...

num_of_days = [0, 31, 28, 31, 30, 31, ...]
    if  and d > num_of_days?:
        m += 1
        d = 1'''




'''if dir_num == 0:
    x = x + 1
    y = y + 0
elif dir_num == 1:
    x=x + 0
    y = y (- 1)


    ...

   dx = [1, 0, -1, 0]
   dy = [0, -1, 0, 1]   #동남서북
   
   
   
    if dir_num == ?:
        x = x + ?
        y = y + ?     

    x = x + dx[dir_num]
    y = y + dy[dir_num]'''

    

'''n = int(input())
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

while n-= 1:'''


dirs = ['W', 'S', 'N', 'E']

dx = [-1,  0,  0,  1]
dy = [ 0, -1, +1,  0]

x, y = 0, 0

# 입력 받기
N = int(input().strip())
for _ in range(N):
    direction, dist = input().split()
    dist = int(dist)
    # 4) direction에 해당하는 인덱스 찾기
    idx = dirs.index(direction)
    # 5) 이동
    x += dx[idx] * dist
    y += dy[idx] * dist

# 6) 결과 출력
print(x, y)
    