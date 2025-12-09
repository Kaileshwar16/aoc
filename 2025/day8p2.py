def solve2(filename):
    pts = []
    with open(filename) as f:
        for line in f:
            x,y,z = map(int, line.split(','))
            pts.append((x,y,z))

    n = len(pts)

    parent = list(range(n))
    size = [1]*n
    comps = n

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a,b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    edges = []
    for i in range(n):
        xi, yi, zi = pts[i]
        for j in range(i+1, n):
            xj, yj, zj = pts[j]
            dx = xi-xj
            dy = yi-yj
            dz = zi-zj
            d2 = dx*dx + dy*dy + dz*dz
            edges.append((d2, i, j))

    edges.sort()

    last_i = last_j = None

    for _, i, j in edges:
        if union(i,j):
            last_i, last_j = i, j
            comps -= 1
            if comps == 1:
                break

    return pts[last_i][0] * pts[last_j][0]


print(solve2("input8.txt"))
