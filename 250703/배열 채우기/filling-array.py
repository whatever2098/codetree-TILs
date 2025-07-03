arr = []

while len(arr) < 10:
    tokens = input().split()
    for tok in tokens:
        x = int(tok)
        if x == 0:
            break_flag = True
            break
        arr.append(x)
        if len(arr) == 10:
            break
        else:
            continue
        break


for val in reversed(arr):
    print(val, end=" ")