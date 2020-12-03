eingabe = open('C:/Users/mikel/Documents/Repos/advent/0301/data.txt', 'r') 
lines = [line.replace("\n","") for line in eingabe]

right = 1
down = 2
posx = 0 
posy = 0
trees = 0


for i in range(0,len(lines),down):
    if lines[i][posx] == "#":
        trees = trees + 1
    posx = (posx + right)%len(lines[0])
    

print(trees)