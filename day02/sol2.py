
with open("./input.txt", "r") as f:
    content = f.readlines()
content = [x.strip() for x in content]


def is_pass_valid(rule, password):
    password = password.strip()
    char_to_check = rule[-1]
    first_entry, second_entry = map(int, rule[:-1].split("-"))

    if first_entry > len(password):
        return False
    elif second_entry > len(password):
        char_1, char_2 = password[first_entry-1], "*"
    else:
        char_1, char_2 = password[first_entry-1], password[second_entry-1]

    print(char_1, char_2, char_to_check)
    if char_1 == char_to_check and char_2 == char_to_check:
        return False
    elif char_1 != char_to_check and char_2 != char_to_check:
        return False
    else:
        return True





count = 0
for line in content:
    rule, psw = line.split(":")

    print("\n")
    print(rule, psw, is_pass_valid(rule, psw))


    if is_pass_valid(rule, psw):
        count += 1

print(count)
