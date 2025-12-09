def solve_part_two(filename="input5.txt"):
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: input.txt not found.")
        return

    ranges_section = content.strip().split('\n\n')[0].strip().split('\n')
    
    parsed_ranges = []
    for line in ranges_section:
        if not line:
            continue
        try:
            start, end = map(int, line.split('-'))
            parsed_ranges.append((start, end))
        except ValueError:
            continue
    
    parsed_ranges.sort(key=lambda x: x[0])
    
    if not parsed_ranges:
        print(0)
        return

    merged_ranges = []
    current_start, current_end = parsed_ranges[0]

    for next_start, next_end in parsed_ranges[1:]:
        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end
    
    merged_ranges.append((current_start, current_end))
    
    total_fresh_ids = 0
    for start, end in merged_ranges:
        total_fresh_ids += (end - start + 1)
        
    print(total_fresh_ids)

if __name__ == "__main__":
    solve_part_two()
