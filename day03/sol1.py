RIGHT = 3
DOWN = 1
TREE = "#"

with open("./input.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]


index = 0
count = 0
for x in content:
    print(x, index+1, x[index], x[index] == TREE)
    if x[index] == TREE:
        count += 1
    index = (index + RIGHT) % len(x)

print(count)

