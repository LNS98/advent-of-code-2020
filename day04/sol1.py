
with open("./input.txt", "r") as f:
    txt = f.read()

data = txt.split("\n\n")


def is_valid(d):
    if len(d) == 8:
        return True
    elif len(d) == 7 and "cid" not in d:
        return True
    else:
        return False


# put each passport in a dict
valid = 0
for p in data:
    x = p.replace("\n", " ")
    d = {entry.split(":")[0]: entry.split(":")[1] for entry in x.split()}

    if is_valid(d):
        valid += 1


print(valid)
