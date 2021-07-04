TREE = "#"

with open("./input.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]



def num_trees_in_slope(content, right, down):
    index = 0
    count = 0
    for i in range(0, len(content), down):
        x = content[i]
        if x[index] == TREE:
            count += 1
        index = (index + right) % len(x)
    return count


rights = [1, 3, 5, 7, 1]
downs = [1, 1, 1, 1, 2]
tot = 1
for r, d in zip(rights, downs):
    tot *= num_trees_in_slope(content, r, d)

print(tot)
