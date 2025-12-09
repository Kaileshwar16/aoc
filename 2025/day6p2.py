def solve_part2(filename):
    # Read the worksheet
    with open(filename) as f:
        lines = [line.rstrip("\n") for line in f]

    # Build rectangular grid
    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]
    height = len(grid)

    # ---------- Step 1: find problem slices (same as part 1) ----------
    slices = []
    start = None

    for col in range(width):
        # check if this column is completely blank
        blank = True
        for row in range(height):
            if grid[row][col] != ' ':
                blank = False
                break

        if blank:
            if start is not None:
                slices.append((start, col - 1))
                start = None
        else:
            if start is None:
                start = col

    if start is not None:
        slices.append((start, width - 1))

    # ---------- Step 2: evaluate each problem using column-wise numbers ----------
    total = 0

    for s, e in slices:
        # operator is in the last row within this slice
        op_chunk = grid[-1][s:e+1]
        if '+' in op_chunk:
            op = '+'
        else:
            op = '*'

        nums = []

        # read one column at a time from RIGHT to LEFT
        for c in range(e, s - 1, -1):
            digits = []

            # collect digits from top to just above operator row
            for r in range(height - 1):
                ch = grid[r][c]
                if ch != ' ':
                    digits.append(ch)

            if digits:
                # top digit is most significant
                n = int("".join(digits))
                nums.append(n)

        # compute value of this problem
        if op == '+':
            value = 0
            for x in nums:
                value += x
        else:
            value = 1
            for x in nums:
                value *= x

        total += value

    return total

print(solve_part2("input6.txt"))
