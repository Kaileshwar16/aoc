
def solve2(filename):
    with open(filename) as f:
        grid = [line.rstrip("\n") for line in f]

    h = len(grid)
    w = len(grid[0]) if h > 0 else 0

    sr = sc = None
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'S':
                sr, sc = r, c
                break
        if sr is not None:
            break

    curr = [0] * w
    curr[sc] = 1
    r = sr
    ans = 0

    while r < h - 1 and any(curr):
        nxt = [0] * w
        nr = r + 1
        for c in range(w):
            v = curr[c]
            if not v:
                continue
            cell = grid[nr][c]
            if cell == '^':
                if c - 1 >= 0:
                    nxt[c - 1] += v
                if c + 1 < w:
                    nxt[c + 1] += v
            else:
                nxt[c] += v
        curr = nxt
        r = nr

    ans += sum(curr)
    return ans

print(solve2("input7.txt"))
