import sys

# Increase recursion depth for deep search trees
sys.setrecursionlimit(2000)

def parse_input(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print("Error: input12.txt not found.")
        sys.exit(1)

    blocks = content.split('\n\n')
    shape_blocks = blocks[:-1]
    query_lines = blocks[-1].strip().split('\n')
    
    shapes = []
    for block in shape_blocks:
        lines = block.strip().split('\n')
        if ':' in lines[0]: lines = lines[1:]
        cells = set()
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == '#': cells.add((r, c))
        shapes.append(cells)
    return shapes, query_lines

def normalize(cells):
    if not cells: return tuple()
    sorted_cells = sorted(list(cells))
    first_r, first_c = sorted_cells[0]
    return tuple(sorted([(r - first_r, c - first_c) for r, c in cells]))

def get_variations(base_cells):
    variations = set()
    def rotate(cells): return {(c, -r) for r, c in cells}
    def flip(cells): return {(r, -c) for r, c in cells}
    curr = base_cells
    for _ in range(4):
        variations.add(normalize(curr))
        variations.add(normalize(flip(curr)))
        curr = rotate(curr)
    return list(variations)

def solve_puzzle():
    shapes, queries = parse_input('input12.txt')
    
    # Precompute variations and sizes
    shape_vars = [get_variations(s) for s in shapes]
    shape_sizes = [len(s) for s in shapes]
    
    solved_count = 0
    print(f"Processing {len(queries)} regions...")

    for q_line in queries:
        if not q_line.strip(): continue
        
        left, right = q_line.split(':')
        W, H = map(int, left.split('x'))
        counts = list(map(int, right.strip().split()))
        
        # Build flattened piece list
        # List of (shape_id, size)
        piece_list = []
        for s_id, count in enumerate(counts):
            for _ in range(count):
                piece_list.append((s_id, shape_sizes[s_id]))
        
        # OPTIMIZATION 1: Sort pieces by Size (Largest first)
        # This fills big chunks early, failing faster if they don't fit.
        piece_list.sort(key=lambda x: x[1], reverse=True)
        
        piece_ids = [p[0] for p in piece_list]
        total_pieces = len(piece_ids)
        total_area = sum(p[1] for p in piece_list)
        grid_area = W * H

        # Quick Prune: Area check
        if total_area > grid_area:
            continue

        # Generate valid bitmasks for every shape ID
        # placements[s_id] = list of (mask, anchor_index)
        placements = {}
        unique_ids = set(piece_ids)
        
        for s_id in unique_ids:
            masks = []
            for var in shape_vars[s_id]:
                # Dimensions of this variation
                max_r = max(r for r, c in var)
                max_c = max(c for r, c in var)
                
                # Iterate all top-left positions (r,c)
                # Bounds check: r + max_r < H, c + max_c < W
                for r in range(H - max_r):
                    for c in range(W - max_c):
                        mask = 0
                        valid = True
                        # anchor is the bit index of the (0,0) cell of the shape
                        # relative to the grid (r, c)
                        anchor = r * W + c 
                        
                        for dr, dc in var:
                            # Verify bounds for every cell (redundant given loop ranges, but safe)
                            nr, nc = r + dr, c + dc
                            bit_idx = nr * W + nc
                            mask |= (1 << bit_idx)
                        
                        masks.append((mask, anchor))
            
            # Sort by anchor (helps with symmetry breaking logic)
            # Use set to remove duplicate masks from symmetries
            unique_masks = sorted(list(set(masks)), key=lambda x: x[1])
            placements[s_id] = unique_masks

        # Memoization cache: stores (piece_index, grid_mask)
        memo = set()

        def backtrack(idx, current_mask, last_anchor):
            # Base Case: All pieces placed
            if idx == total_pieces:
                return True
            
            # State for memoization
            state = (idx, current_mask)
            if state in memo:
                return False
            
            s_id = piece_ids[idx]
            
            # OPTIMIZATION 2: Symmetry Breaking for Identical Pieces
            # If current piece is same type as previous, enforce ordering
            # Previous piece was placed at 'last_anchor'. 
            # Current piece must be placed at an anchor > last_anchor.
            start_search_index = 0
            is_same_as_prev = (idx > 0 and piece_ids[idx] == piece_ids[idx-1])
            
            valid_moves = placements[s_id]
            
            for mask, anchor in valid_moves:
                # Symmetry constraint
                if is_same_as_prev and anchor <= last_anchor:
                    continue
                
                # Collision check
                if (current_mask & mask) == 0:
                    # Recurse
                    if backtrack(idx + 1, current_mask | mask, anchor):
                        return True
            
            # If no move worked, mark state as failed
            memo.add(state)
            return False

        # Start search
        if backtrack(0, 0, -1):
            solved_count += 1
            # print(f"Region {W}x{H} Solved.")
        else:
            pass
            # print(f"Region {W}x{H} Impossible.")

    print(f"Answer: {solved_count}")

if __name__ == "__main__":
    solve_puzzle()
