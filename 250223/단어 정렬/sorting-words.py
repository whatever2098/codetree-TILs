n = int(input())
word = [input() for _ in range(n)]

word.sort()
for i in range(n):
    print(word[i])