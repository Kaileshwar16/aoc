with open("input.txt", "r") as f:
    lines = f.read().splitlines()

val = 50        # dial starts at 50
pwd = 0         # password count

for line in lines:
    direction = line[0]
    dist = int(line[1:])      # number part
    
    if direction.lower() == "l":
        val = (val - dist) % 100
    else:  # R
        val = (val + dist) % 100

    if val == 0:
        pwd += 1

print(pwd)
