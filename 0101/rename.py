import itertools
eingabe = open('C:/Users/mikel/Documents/Repos/advent/01/eingabe.txt', 'r') 
lines = eingabe.readlines()
liste = []

solution = 0
for line in lines:
    line[-2:0]
    line = int(line)
    liste.append(line)


for a, b in itertools.combinations(liste, 2):
    summe = a + b
    if summe == 2020:
        solution = a * b
        print(solution)
