def max_subsequence_of_length_k(s, k):
    n = len(s)
    drop = n - k
    stack = []
    for ch in s.strip():
        while drop > 0 and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)
    return ''.join(stack[:k])

def total_joltage(filename, k=12):
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            best = max_subsequence_of_length_k(line, k)
            total += int(best)
    return total

print(total_joltage("input3p2.txt", 12))
