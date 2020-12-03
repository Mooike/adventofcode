eingabe = open('C:/Users/mikel/Documents/Repos/advent/0301/data.txt', 'r') 
lines = eingabe.readlines()
karte = []
counter = 0
trees = 0

for line in lines:
    line = line.replace("\n", "")
    kette = []
    for i in range(0,42):
        kette.append(line)
    kette = "".join(kette)
    karte.append(kette)
    


for line in karte:
    objekt = line[counter*3]
    
    if objekt == "#":
        trees = trees + 1
    counter = counter + 1

print(trees)


