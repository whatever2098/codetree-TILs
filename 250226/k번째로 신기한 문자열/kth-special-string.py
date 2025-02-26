n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

strs = list()
for one_str in str:
    include_t = True
    for i in range (len(t)):
        if one_str[i] != t[i]:
            include_t = False
            break
    
    if include_t:
        strs.append(one_str)

strs.sort()
print(strs[k - 1])