#!/usr/bin/env python3

import sys


def is_infinite(rows: list[list[str]], guard_position: tuple[int, int]) -> bool:
    visited_spots = set()

    while True:
        x, y = guard_position
        orientation = rows[x][y]

        # Check if we have been in this position, with this orientation
        if (x, y, orientation) in visited_spots:
            # We have, there's an infinite loop
            return True

        # Add current position to visited spots
        visited_spots.add((x, y, orientation))

        match orientation:
            # Move up
            case "^":
                # Check if we are moving out ot labyrinth and escaping
                if x == 0:
                    return False

                new_x = x - 1
                new_y = y
                new_orientation = ">"
            # Move left
            case "<":
                # Check if we are moving out ot labyrinth and escaping
                if y == 0:
                    return False

                new_x = x
                new_y = y - 1
                new_orientation = "^"
            # Move right
            case ">":
                # Check if we are moving out ot labyrinth and escaping
                if y + 1 >= len(rows[x]):
                    return False

                new_x = x
                new_y = y + 1
                new_orientation = "v"
            # Move down
            case "v":
                # Check if we are moving out ot labyrinth and escaping
                if x + 1 >= len(rows):
                    return False

                new_x = x + 1
                new_y = y
                new_orientation = "<"

        # Check is the new space would be empty?
        if rows[new_x][new_y] == ".":
            # Move to the empty space
            rows[new_x][new_y] = orientation
            rows[x][y] = "."
            guard_position = (new_x, new_y)
        else:
            # Turn
            rows[x][y] = new_orientation


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

    # Strip newline, create list of lists
    rows = [list(x.strip()) for x in input_lines]

    # Find initial guard position
    guard_position = find_guard_position(rows)

    # How many alternations are infinite?
    total = 0

    # Iterate rows
    for row in range(len(rows)):
        # Iterate columns
        for col in range(len(rows[row])):
            # Check if we can place an obstacle
            if rows[row][col] != ".":
                continue

            # Copy rows
            new_rows = [r[:] for r in rows]
            # Mark new obstacle
            new_rows[row][col] = "#"

            if is_infinite(new_rows, guard_position):
                total += 1

    print(total, "OK" if total == 1767 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
