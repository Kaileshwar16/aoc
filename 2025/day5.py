ranges = []
ingredients = []

with open("input5.txt") as f:
    lines = [line.rstrip("\n") for line in f]

sep_index = None
for idx, line in enumerate(lines):
    if line.strip() == "":
        sep_index = idx
        break

if sep_index is None:
    raise RuntimeError("No blank line found")

range_lines = lines[:sep_index]
ingredient_lines = lines[sep_index + 1:]

for r in range_lines:
    start, end = map(int, r.split("-"))
    ranges.append((start, end))

ingredients = [int(x) for x in ingredient_lines if x.strip() != ""]

fresh_count = 0

for id_ in ingredients:
    for a, b in ranges:
        if a <= id_ <= b:
            fresh_count += 1
            break

print(fresh_count)
