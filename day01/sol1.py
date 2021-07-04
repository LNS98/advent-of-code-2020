import os


with open("./input.txt", "r") as f:
    txt = f.read()


data = txt.split("\n")
del data[-1]
data = sorted(list(map(int, data)))

print(txt)
print(data)


def brute_force(data):
    for i in data:
        for j in data:
            if i == j:
                continue
            if i + j == 2020:
                return i, j


i, j = brute_force(data)
print(i, j, i * j)
