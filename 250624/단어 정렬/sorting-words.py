n = int(input())
word = [input() for _ in range(n)]

word.sort()

for x in word:
    print(x)