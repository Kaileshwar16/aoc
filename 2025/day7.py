
def solve(filename):
    with open(filename) as f:
        grid = [line.rstrip("\n") for line in f]

    h = len(grid)
    w = len(grid[0])

    sr = sc = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                sr, sc = r, c
                break
        if sr is not None:
            break

    beams = {(sr, sc)}
    splits = 0

    while beams:
        nxt = set()
        for r, c in beams:
            nr = r + 1
            if nr >= h:
                continue
            cell = grid[nr][c]
            if cell == '^':
                splits += 1
                if c - 1 >= 0:
                    nxt.add((nr, c - 1))
                if c + 1 < w:
                    nxt.add((nr, c + 1))
            else:
                nxt.add((nr, c))
        beams = nxt

    return splits


print(solve("input7.txt"))
