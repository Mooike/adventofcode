with open("data") as f:
    data = f.read().replace("\n", " ")

bps = data.split(" ")

seatids = []

for bp in bps:
    row, col = 0, 0
    start = 0 
    end = 127
    r = bp[:7]
    for char in r:
        if char == "F":
            end = int((start+end+1)/2) - 1
        if char == "B":
            start = int((start+end+1)/2)
        
    row = start

    s = bp[7:]
    start = 0 
    end = 7 

    for char in s: 
        if char == "L":
            end = int((start+end+1)/2) - 1
        if char == "R":
            start = int((start+end+1)/2)
    col = start

    sid = row * 8 + col

    seatids.append(sid)


print("highest id: ", max(seatids))