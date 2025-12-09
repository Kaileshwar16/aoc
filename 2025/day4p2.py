def solve_part_two(filename):
    # Read the input file
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Please create the file with your puzzle input.")
        return

    # Parse grid into a set of coordinates {(row, col), ...}
    # Using a set is much faster for lookups and removal than a list of lists
    papers = set()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '@':
                papers.add((r, c))

    total_removed = 0
    round_count = 0
    
    # Directions for 8 neighbors (vertical, horizontal, diagonal)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    while True:
        round_count += 1
        to_remove = set()

        # Check every current paper roll
        for r, c in papers:
            neighbor_count = 0
            
            # Count how many neighbors are also paper rolls
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in papers:
                    neighbor_count += 1
            
            # Condition: accessible if fewer than 4 neighbors
            if neighbor_count < 4:
                to_remove.add((r, c))

        # If nothing to remove, we are done
        if not to_remove:
            break

        # Update the state
        count = len(to_remove)
        total_removed += count
        
        # Remove the identified papers from the main set
        papers -= to_remove

        # Optional: Print progress
        # print(f"Round {round_count}: Removed {count} rolls")

    print(f"Total rolls removed: {total_removed}")

if __name__ == "__main__":
    solve_part_two("input4p2.txt")
