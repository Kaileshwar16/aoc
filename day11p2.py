import sys
from functools import cache

# Increase recursion depth for deep graphs
sys.setrecursionlimit(20000)

def solve():
    adj = {}
    
    # 1. Parse the input
    try:
        with open("input11.txt") as f:
            for line in f:
                if not line.strip(): continue
                parts = line.strip().split(': ')
                node = parts[0]
                # If a node has no outputs listed, it might look like "node:" or just handle missing part
                neighbors = parts[1].split() if len(parts) > 1 else []
                adj[node] = neighbors
    except FileNotFoundError:
        print("Error: input.txt not found.")
        return

    # 2. DP Function with Memoization
    # Returns the number of paths from current_node to target_node
    @cache
    def count_paths(u, target):
        if u == target:
            return 1
        
        # If u is a terminal node (like 'out') or not in our map
        if u not in adj:
            return 0
        
        total = 0
        for v in adj[u]:
            total += count_paths(v, target)
        return total

    # 3. Calculate paths for Sequence A: svr -> dac -> fft -> out
    s_to_dac = count_paths('svr', 'dac')
    dac_to_fft = count_paths('dac', 'fft')
    fft_to_out = count_paths('fft', 'out')
    
    path_a_count = s_to_dac * dac_to_fft * fft_to_out

    # 4. Calculate paths for Sequence B: svr -> fft -> dac -> out
    s_to_fft = count_paths('svr', 'fft')
    fft_to_dac = count_paths('fft', 'dac')
    dac_to_out = count_paths('dac', 'out')
    
    path_b_count = s_to_fft * fft_to_dac * dac_to_out

    # 5. Output Result
    print(f"Paths visiting dac then fft: {path_a_count}")
    print(f"Paths visiting fft then dac: {path_b_count}")
    print(f"Total Part 2 Answer: {path_a_count + path_b_count}")

if __name__ == '__main__':
    solve()
