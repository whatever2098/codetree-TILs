n = int(input())

answer = []
while n > 0:
    answer.append(n % 2)
    n //=2:

for x in answer[::-1]:
    print(x)
