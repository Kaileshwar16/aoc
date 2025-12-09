
def solve(filename):
    # Read file
    with open(filename) as f:
        lines = [line.rstrip("\n") for line in f]

    # Pad lines to same width
    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    height = len(grid)

    # ---- Step 1: Find column slices for each problem ----
    slices = []
    start = None

    for col in range(width):
        # Check if column is fully blank
        blank = True
        for row in range(height):
            if grid[row][col] != ' ':
                blank = False
                break

        if blank:
            if start is not None:        # close current slice
                slices.append((start, col - 1))
                start = None
        else:
            if start is None:            # open new slice
                start = col

    if start is not None:                # last slice
        slices.append((start, width - 1))

    # ---- Step 2: Evaluate each problem ----
    total = 0

    for s, e in slices:
        # operator is in the last row
        op_chunk = grid[-1][s:e+1]
        if '+' in op_chunk:
            op = '+'
        else:
            op = '*'

        # collect numbers from above rows
        nums = []
        for r in range(height - 1):
            chunk = grid[r][s:e+1].strip()
            if chunk:
                nums.append(int(chunk))

        # compute
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

print(solve("input6.txt"))
