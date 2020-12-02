eingabe = open('C:/Users/mikel/Documents/Repos/advent/0201/data.txt', 'r') 
lines = eingabe.readlines()
valid_counter=0 
for line in lines:
    elemente = []
    line = line.split(" ")
    anzahl = line[0]    
    anzahl = anzahl.split("-")   
    lower = int(anzahl[0])
    upper = int(anzahl[1])
    r = []
    for i in range(lower,upper+1):
        r.append(i)
    buchstabe = line[1]
    buchstabe = buchstabe[0]

    password = line[2]
    counter = 0 
    for char in password:
        if char == buchstabe:
            counter = counter + 1
    if counter in r:
        valid_counter = valid_counter + 1
    
print(valid_counter)

    