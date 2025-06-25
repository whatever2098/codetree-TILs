n = int(input())
name = []
height = []
weight = []

people = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))
    people.append((n_i, int(h_i), int(w_i)))

people.sort(key=lambda x: x[1] )

for n_i, h_i, w_i in people:
    print(n_i, str(h_i), str(w_i))

