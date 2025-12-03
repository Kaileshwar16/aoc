with open("input3.txt", "r") as f:
    lines = f.read().splitlines()

total = 0

for line in lines:
    maximum = 99  # reset for each line

    while maximum >= 10:
        found = False
        target = str(maximum)

        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if line[i] + line[j] == target:
                    total += maximum
                    found = True
                    break
            if found:
                break

        if found:
            break  # go to next line
        else:
            maximum -= 1  # check next smaller number

print(total)
