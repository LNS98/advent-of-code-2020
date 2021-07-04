ROWS = 128
COLUMNS = 8

with open("./input.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]

def convert_to_bin(values, one, zero):
    return int("0b" + values.replace(one, "1").replace(zero, "0"), 2)

seen_ids = []
for bp in content:
    row, col = convert_to_bin(bp[:-3], "B", "F"), convert_to_bin(bp[-3:], "R", "L")
    id_ = row * 8 + col
    seen_ids.append(id_)

all_ids = [8*row + col for row in range(ROWS) for col in range(COLUMNS)]

print(set(all_ids)-set(seen_ids))
