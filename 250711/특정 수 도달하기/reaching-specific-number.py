nums = list(map(int, input().split()))

total = 0
count = 0

for x in nums:
    if x >= 250:
        break
    total += x
    count += 1 

average = total / count
print(f"{total} {average}")