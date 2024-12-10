#!/usr/bin/env python3

import sys


def path(m: list[list[int]], pos: tuple[int, int]) -> list[list[tuple[int, int]]]:
    current_value = m[pos[0]][pos[1]]

    # Trail end, don't travel anymore
    if current_value == 9:
        return [[pos]]

    found_paths = []
    next_value = current_value + 1

    # Up
    if pos[0] > 0 and m[pos[0] - 1][pos[1]] == next_value:
        found_paths.extend(path(m, (pos[0] - 1, pos[1])))
    # Down
    if pos[0] < len(m) - 1 and m[pos[0] + 1][pos[1]] == next_value:
        found_paths.extend(path(m, (pos[0] + 1, pos[1])))
    # Left
    if pos[1] > 0 and m[pos[0]][pos[1] - 1] == next_value:
        found_paths.extend(path(m, (pos[0], pos[1] - 1)))
    # Right
    if pos[1] < len(m[pos[0]]) - 1 and m[pos[0]][pos[1] + 1] == next_value:
        found_paths.extend(path(m, (pos[0], pos[1] + 1)))

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
                start_positions.append((x, y))

    total = 0
    for start_position in start_positions:
        # Find paths from all start positions
        paths = path(trailmap, start_position)

        # Convert to unique end positions
        unique_end_positions = set([p[-1] for p in paths])

        # Update total with the score (number of unique end positions)
        total += len(unique_end_positions)

    print(total, "OK" if total == 624 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
