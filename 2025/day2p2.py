
with open("input2p2.txt", "r") as f:
    content = f.read().strip()

ranges = content.split(",")

total = 0

def invalid(num):
    s = str(num)
    L = len(s)

    # try all chunk sizes
    for k in range(1, L):  
        if L % k != 0:
            continue

        chunk = s[:k]
        if chunk * (L // k) == s:
            return True

    return False


for r in ranges:
    start, end = map(int, r.split("-"))
    for i in range(start, end + 1):
        if invalid(i):
            total += i

print(total)
