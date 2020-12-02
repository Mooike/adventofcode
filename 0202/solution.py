eingabe = open('C:/Users/mikel/Documents/Repos/advent/0202/data.txt', 'r') 
lines = eingabe.readlines()

valid_counter=0 
for line in lines:
    line = line.split(" ")
    anzahl = line[0]    
    anzahl = anzahl.split("-")   
    first = int(anzahl[0])
    first = first -1
    second = int(anzahl[1])
    second = second -1
    password = line[2]
    password.replace("\n", "")
    
    buchstabe = line[1]
    buchstabe = buchstabe[0] 
    
    if password[first] == buchstabe and password[second] != buchstabe:
        valid_counter = valid_counter + 1 
    if password[first] != buchstabe and password[second] == buchstabe:   
        valid_counter = valid_counter + 1    
print(valid_counter)
