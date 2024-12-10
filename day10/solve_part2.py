#!/usr/bin/env python3

import sys
from collections import namedtuple


Coord = namedtuple("Coord", ["x", "y"])


def path(m: list[list[int]], pos: Coord) -> list[list[Coord]]:
    current_value = m[pos.x][pos.y]

    # Trail end, don't travel anymore
    if current_value == 9:
        return [[pos]]

    found_paths = []
    next_value = current_value + 1

    # Up
    if pos.x > 0 and m[pos.x - 1][pos.y] == next_value:
        found_paths.extend(path(m, Coord(pos.x - 1, pos.y)))
    # Down
    if pos.x < len(m) - 1 and m[pos.x + 1][pos.y] == next_value:
        found_paths.extend(path(m, Coord(pos.x + 1, pos.y)))
    # Left
    if pos.y > 0 and m[pos.x][pos.y - 1] == next_value:
        found_paths.extend(path(m, Coord(pos.x, pos.y - 1)))
    # Right
    if pos.y < len(m[pos.x]) - 1 and m[pos.x][pos.y + 1] == next_value:
        found_paths.extend(path(m, Coord(pos.x, pos.y + 1)))

    # Create and return new valid paths with current position
    return [[pos] + found_path for found_path in found_paths]


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    # Strip newlines
    lines = [x.strip() for x in input_lines]

    trailmap = []
    start_positions = []

    # Iterate each line
    for x, line in enumerate(lines):
        # Convert string of digits to list of ints
        trailmap.append(list(map(int, line)))

        # Check if this line contains any start positions
        for y, char in enumerate(trailmap[x]):
            if trailmap[x][y] == 0:
                start_positions.append(Coord(x, y))

    total = 0
    for start_position in start_positions:
        # Find paths from all start positions
        paths = path(trailmap, start_position)

        # Update total with the number of paths found
        total += len(paths)

    print(total, "OK" if total == 1483 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
