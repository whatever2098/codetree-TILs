sum = 0
divisor = 0

arr = [map(int, input().split())]

for i in range(10):
    if i >= 250:
        break
    sum += arr[i]
    divisor += 1


print(str(sum) + str(round(sum / divisor)))
