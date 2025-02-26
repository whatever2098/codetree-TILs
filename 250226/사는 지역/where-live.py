n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

class Person:
    def __init__(self, name, street_address, region):
        self.n = name
        self.s = street_address
        self.r = region

people = []
people = [Person(name[i], street_address[i], region[i]) for i in range(n)]

for person in people:
    if person.n == sorted(name, reverse = True)[0]:
        print("name", person.n)
        print("addr", person.s)
        print("city", person.r)
