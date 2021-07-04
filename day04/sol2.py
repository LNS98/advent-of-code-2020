
with open("./input.txt", "r") as f:
    txt = f.read()

data = txt.split("\n\n")


class Passport:
    def __init__(self, data):
        self.p = data

    def __str__(self):
        return f"{self.p}"

    def is_valid(self):
        if len(self.p) == 8:
            return self._check_all_rules()
        elif len(self.p) == 7 and "cid" not in d:
            return self._check_all_rules()
        else:
            return False

    def _check_all_rules(self):
        if not self._check_birth():
            return False
        if not self._check_issue():
            return False
        if not self._check_expiration():
            return False
        if not self._check_height():
            return False
        if not self._check_hair_colour():
            return False
        if not self._check_eye_colour():
            return False
        if not self._check_id():
            return False
        return True

    def _check_birth(self):
        return self._check_numeric(self.p["byr"], 1920, 2002)

    def _check_issue(self):
        val = self.p["iyr"]
        if len(val) != 4:
            return False
        return self._check_numeric(val, 2010, 2020)

    def _check_expiration(self):
        val = self.p["eyr"]
        if len(val) != 4:
            return False
        return self._check_numeric(val, 2020, 2030)

    def _check_height(self):
        val = self.p["hgt"]
        if val.endswith("cm"):
            return self._check_numeric(val.strip("cm"), 150, 193)
        elif val.endswith("in"):
            return self._check_numeric(val.strip("in"), 59, 76)
        return False

    def _check_hair_colour(self):
        val = self.p["hcl"]
        if val.startswith("#"):
            val = val[1:]
            if len(val) != 6:
                return False
            return all(
                ord("a") <= ord(c) <= ord("f") or ord("0") <= ord(c) <= ord("9")
                for c in val
            )
        else:
            return False

    def _check_eye_colour(self):
        valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.p["ecl"] in valid_colours

    def _check_id(self):
        return len(self.p["pid"]) == 9 and self.p["pid"].isdigit()

    def _check_numeric(self, val, min_year, max_year):
        if val.isdigit():
            val = int(val)
            return min_year <= val <= max_year
        else:
            return False


# put each passport in a dict
valid = 0
for p in data:
    x = p.replace("\n", " ")
    d = {entry.split(":")[0]: entry.split(":")[1] for entry in x.split()}
    p = Passport(d)

    if p.is_valid():
        valid += 1


print(valid)
