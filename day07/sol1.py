
with open("./input.txt", "r") as f:
    data = f.read()

data = data.split("\n")


def get_contain_rules(x):
    x = x.strip().strip(".").strip("bags")
    return x[0] * list(x[1:])

# make data of rules with the key as the bag colour and a list of what it
# contains as values
rules = {}
for rule in data:
    key = rule.split("bag")[0].strip()
    values = list(map(lambda x: x.strip(), rule.split("contain")[-1].split(",")))
    print(key, values, "RULE: ", rule)
