with open("input2.txt", "r") as f:
    content = f.read().strip()

rnges =  content.split(",")


def check(words):
    s = str(words)
    if len(s) % 2 != 0:   # must be even
        return 0
    mid = len(s) // 2
    if s[:mid] == s[mid:]:
        return int(s)     # return FULL number
    return 0

sum = 0
for rnge in rnges:
    start, end = rnge.split("-")
    for i in range(int(start), int(end)+1):
        sum+=check(i)
print(sum)

