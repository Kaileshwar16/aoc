with open("input.txt", "r") as f:
    lines = f.read().splitlines()

val = 50        # dial starts at 50
pwd = 0         # password count

for line in lines:
    direction = line[0]
    dist = int(line[1:])

    step = 1 if direction == "R" else -1

    for _ in range(dist):
        val = (val + step) % 100   # wrap around the dial
        if val == 0:
            pwd += 1               # count click hitting zero

print(pwd)
