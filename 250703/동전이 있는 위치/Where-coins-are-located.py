n, m = map(int, input().split())

placed = [[0 for _ in range(n)] for _ in range(n)]
#0 ~ (n - 1)

for _ in range(m):
    r, c = map(int, input().split())
    placed[r - 1][c - 1] = 1
    
for i in range(n):      
    for j in range(n):
        if placed[i][j] == 1:
            print(str(1) , end = " ")
        else: print(str(0) , end = " ")
    print()