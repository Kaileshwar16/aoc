from functools import reduce
import math
from pathlib import Path
from collections import Counter
from itertools import combinations
from shapely.geometry import Polygon, box
from shapely.prepared import prep

input_path = Path(__file__).parent / "input9.txt"

type Point = tuple[int, int]

def parse_input(text: str) -> list[Point]:
    lines = text.strip().split("\n")
    coords: list[Point] = []
    for line in lines:
        if not line.strip():
            continue
        x_str, y_str = line.split(",")
        coords.append((int(x_str), int(y_str)))
    return coords

def max_rectangle_area_part2(points: list[Point]) -> int:
    n = len(points)
    if n < 2:
        return 0

    poly = Polygon(points)
    prepared_poly = prep(poly)

    max_area = 0
    for (x1, y1), (x2, y2) in combinations(points, 2):
        min_x, max_x = (x1, x2) if x1 <= x2 else (x2, x1)
        min_y, max_y = (y1, y2) if y1 <= y2 else (y2, y1)

        width = max_x - min_x + 1
        height = max_y - min_y + 1
        area = width * height

        if area <= max_area:
            continue

        rect = box(min_x, min_y, max_x, max_y)

        if prepared_poly.covers(rect):
            max_area = area

    return max_area

def solve(text: str) -> int:
    points = parse_input(text)
    return max_rectangle_area_part2(points)

def main():
    if input_path.exists():
        input_text = input_path.read_text()
        print(solve(input_text))

if __name__ == "__main__":
    main()
