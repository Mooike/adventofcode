import itertools
eingabe = open('C:/Users/mikel/Documents/Repos/advent/01/eingabe.txt', 'r') 
lines = eingabe.readlines()
liste = []
solution = 0
for line in lines:
    line[-2:0]
    line = int(line)
    liste.append(line)

for a, b, c in itertools.combinations(liste, 3):
    summe = a + b + c
    if summe == 2020:
        solution = a * b * c
        print(solution)