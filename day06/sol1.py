with open("./input.txt", "r") as f:
    data = f.read()

data = data.split("\n\n")


all_questions = 0
for group in data:
    all_questions += len(set(group.replace("\n", "")))

print(all_questions)
