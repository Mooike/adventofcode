with open("data") as f:
    raw = f.read().split("\n")

position = [0,0]

for command in raw:
    direction = command[0]
    print(direction)