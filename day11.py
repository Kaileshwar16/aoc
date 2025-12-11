
import sys
from collections import defaultdict

def parse_lines(lines):
    g = defaultdict(list)
    for line in lines:
        line = line.strip()
        if not line:
            continue
        left, right = line.split(':', 1)
        node = left.strip()
        targets = right.strip().split()
        for t in targets:
            g[node].append(t)
    return g

def count_paths(graph, start='you', end='out'):
    stack = [(start, {start})]
    total = 0
    while stack:
        node, visited = stack.pop()
        if node == end:
            total += 1
            continue
        for nbr in graph.get(node, []):
            if nbr in visited:
                continue
            nv = set(visited)
            nv.add(nbr)
            stack.append((nbr, nv))
    return total

def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    graph = parse_lines(lines)
    print(count_paths(graph))

if __name__ == "__main__":
    main()
