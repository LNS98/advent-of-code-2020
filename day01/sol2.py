import os


with open("./input.txt", "r") as f:
    txt = f.read()


data = txt.split("\n")
del data[-1]
data = sorted(list(map(int, data)))

def brute_force(data):
    for i in data:
        for j in data:
            for k in data:
                if i == j or i == k or j == k:
                    continue
                if i + j + k== 2020:
                    return i, j, k


i, j, k = brute_force(data)
print(i, j, k, i * j * k)
