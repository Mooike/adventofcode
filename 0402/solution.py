with open("data") as f:
    raw = f.read().split('\n\n')

passports = []
valid_passports = 0
for passport in raw:
    passport = passport.replace("\n", " ")
    passport = passport.split(" ")
    passDict = {}
    for pair in passport:
        pair = pair.split(":")
        field = pair[0]
        val = pair[1]
        passDict[field] = val

    passports.append(passDict)

reasons = []
for passport in passports:      
    
    valid = True
    reason = []
    if "byr" in passport: 
        year = int(passport.get("byr"))
        if year < 1920 or year > 2002:
            valid = False
            reason.append("byr")
    if not "byr" in passport:
        valid = False
        reason.append("byr")
    if "iyr" in passport: 
        year = int(passport.get("iyr"))
        if year < 2010 or year > 2020:
            valid = False
            reason.append("iyr")
    if not "iyr" in passport:
        valid = False
        reason.append("iyr")
    if "eyr" in passport: 
        year = int(passport.get("eyr"))
        if year < 2020 or year > 2030:
            valid = False
            reason.append("eyr")
    if not "eyr" in passport:
        valid = False
        reason.append("eyr")
    if "hgt" in passport: 
        field = passport.get("hgt")
        if field.isdigit():
            valid = False
            reason.append("hgt")
        else:
            hgt = int(field[:-2])
            unit = field[-2:]
            if unit == "cm":
                if hgt < 150 or hgt > 193:
                    valid = False
            if unit == "in":
                if hgt < 59 or hgt > 76:
                    valid = False
    if not "hgt" in passport:
        reason.append("hgt")
        valid = False

    if "hcl" in passport:
        hairs = passport.get("hcl")
        if not "#" in hairs:
            valid = False
            reason.append("hcl | ###")
        if "#" in hairs:
            toproof = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
            hairs = hairs[1:]
            for char in hairs:
                print(char)
                if not char in toproof:
                    valid = False
    if not "hcl" in passport:
        valid = False
        reason.append("hcl")
    if "ecl" in passport:
        colors = "amb blu brn gry grn hzl oth"
        colors = colors.split(" ")
        color = passport.get("ecl")
        if not color in colors:
            valid = False
            reason.append("ecl")
    if not "ecl" in passport:
        valid = False
        reason.append("ecl")
    if "pid" in passport:
        id = passport.get("pid")
        if id.isdigit():
            if len(id)== 9:
                id = id 
            else:
                valid = False
                reason.append("pid")
        else:
            valid = False
    if not "pid" in passport:
        valid = False
        reason.append("pid")
    if valid:
        valid_passports += 1 
    
    reasons.append(reason)
print("Number of valid passports: ", valid_passports)
