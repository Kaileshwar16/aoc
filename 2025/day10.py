import sys
import re
from collections import deque

def parse_line(line: str):
    line = line.strip()
    if not line:
        return None

    m = re.search(r'\[([.#]+)\]', line)
    if not m:
        raise ValueError(f"Invalid line (no [] pattern): {line}")
    lights_str = m.group(1)
    num_lights = len(lights_str)

    target_mask = 0
    for i, ch in enumerate(lights_str):
        if ch == '#':
            target_mask |= (1 << i)

    after_bracket = line.split(']', 1)[1]
    buttons_part = after_bracket.split('{', 1)[0]

    button_specs = re.findall(r'\(([^)]*)\)', buttons_part)

    button_masks = []
    for spec in button_specs:
        spec = spec.strip()
        if not spec:
            continue
        indices = [int(x) for x in spec.split(',') if x.strip() != ""]
        mask = 0
        for idx in indices:
            if idx < 0 or idx >= num_lights:
                raise ValueError(f"Button index {idx} out of range for {num_lights} lights in line: {line}")
            mask |= (1 << idx)
        button_masks.append(mask)

    return num_lights, target_mask, button_masks


def min_presses_for_machine(num_lights, target_mask, button_masks):
    if target_mask == 0:
        return 0  

    max_state = 1 << num_lights
    dist = [-1] * max_state

    q = deque()
    start = 0
    dist[start] = 0
    q.append(start)

    while q:
        state = q.popleft()
        d = dist[state]

        for mask in button_masks:
            next_state = state ^ mask
            if dist[next_state] == -1:
                dist[next_state] = d + 1
                if next_state == target_mask:
                    return d + 1
                q.append(next_state)

    raise RuntimeError("Target configuration unreachable for a machine")


def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1], "r")
    else:
        f = sys.stdin

    total_presses = 0

    for line in f:
        line = line.rstrip("\n")
        if not line.strip():
            continue  
        parsed = parse_line(line)
        if parsed is None:
            continue
        num_lights, target_mask, button_masks = parsed
        presses = min_presses_for_machine(num_lights, target_mask, button_masks)
        total_presses += presses

    if f is not sys.stdin:
        f.close()

    print(total_presses)


if __name__ == "__main__":
    main()
