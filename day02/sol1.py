
with open("./input.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]


def is_pass_valid(rule, password):
    char_to_check = rule[-1]
    min_val, max_val = map(int, rule[:-1].split("-"))

    return min_val <= sum(1 for char in password if char == char_to_check) <= max_val


count = 0
for line in content:
    rule, psw = line.split(":")
    if is_pass_valid(rule, psw):
        count += 1

print(count)
