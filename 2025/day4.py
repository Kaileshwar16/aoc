# solve_day4.py

def solve():
    with open("input4.txt", "r") as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    # 8 neighbor directions
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1),
    ]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    accessible = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue

            adj = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and grid[nr][nc] == '@':
                    adj += 1

            if adj < 4:
                accessible += 1

    print(accessible)


if __name__ == "__main__":
    solve()
