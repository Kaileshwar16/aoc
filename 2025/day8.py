
import math
from itertools import combinations

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def solve(points, K):
    n = len(points)
    dsu = DSU(n)

    edges = []
    for i, j in combinations(range(n), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        dist2 = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        edges.append((dist2, i, j))

    edges.sort()

    # Process the first K closest pairs
    for idx in range(min(K, len(edges))):
        _, a, b = edges[idx]
        dsu.union(a, b)

    # Compute final component sizes
    comp = {}
    for i in range(n):
        r = dsu.find(i)
        comp[r] = comp.get(r, 0) + 1

    sizes = sorted(comp.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    # Read input
    points = []
    with open("input8.txt") as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            points.append((x, y, z))

    print(solve(points, 1000))
