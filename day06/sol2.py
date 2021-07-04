with open("./input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")

all_questions = 0
for group in data:
    first, *rest = list(map(set, group.strip().split("\n")))
    all_questions += len(first.intersection(*rest))

print(all_questions)
