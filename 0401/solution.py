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


for passport in passports:
    valid = True
    if not "byr" in passport:
        valid = False
    if not "iyr" in passport:
        valid = False
    if not "eyr"  in passport:
        valid = False
    if not "hgt"  in passport:
        valid = False
    if not "hcl"  in passport:
        valid = False
    if not "ecl"  in passport:
        valid = False
    if not "pid"  in passport:
        valid = False
    if valid:
        valid_passports += 1
        

print("Number of invalid passports: ", valid_passports)
        
