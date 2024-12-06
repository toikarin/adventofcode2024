#!/usr/bin/env python3

import sys


def find_guard_position(rows: list[list[str]]) -> tuple[int, int]:
    for i, row in enumerate(rows):
        for j, char in enumerate(row):
            if char in ["v", "^", "<", ">"]:
                return (i, j)

    assert False, "unreachable"


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    # Strip newlines
    rows = [list(x.strip()) for x in input_lines]

    # Find initial guard position
    guard_position = find_guard_position(rows)

    # Unique visited spots
    visited_spots = set()

    # While not espaced
    while True:
        x, y = guard_position
        orientation = rows[x][y]

        match orientation:
            case "^":
                # Check if we are moving out ot labyrinth and escaping
                if x == 0:
                    break

                new_x = x - 1
                new_y = y
                new_orientation = ">"
            case "<":
                # Check if we are moving out ot labyrinth and escaping
                if y == 0:
                    break

                new_x = x
                new_y = y - 1
                new_orientation = "^"
            case ">":
                # Check if we are moving out ot labyrinth and escaping
                if y + 1 >= len(rows[x]):
                    break

                new_x = x
                new_y = y + 1
                new_orientation = "v"
            case "v":
                # Check if we are moving out ot labyrinth and escaping
                if x + 1 >= len(rows):
                    break

                new_x = x + 1
                new_y = y
                new_orientation = "<"

        # Check is the new space would be empty?
        if rows[new_x][new_y] == ".":
            # Move to the empty space
            rows[new_x][new_y] = orientation
            rows[x][y] = "."
            guard_position = (new_x, new_y)

            # Check if we have been in this spot before?
            if (x, y) not in visited_spots:
                visited_spots.add((x, y))
        else:
            # Turn
            rows[x][y] = new_orientation

    total = len(visited_spots) + 1
    print(total, "OK" if total == 5212 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
