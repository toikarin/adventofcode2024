#!/usr/bin/env python3

import sys


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    total = 0
    # Strip newlines
    lines = [x.strip() for x in input_lines]

    # Iterate lines
    for i, line in enumerate(lines):
        # Iterate each char
        for j, char in enumerate(line):
            # No need to search unless current char is A
            if char != "A":
                continue

            # Sanity check for checking the X is possible
            if j < 1 or j + 1 >= len(line) or i < 1 or i + 1 >= len(lines):
                continue

            if (
                # M
                #  A
                #   S
                (lines[i - 1][j - 1] == "M" and lines[i + 1][j + 1] == "S")
                # S
                #  A
                #   M
                or (lines[i - 1][j - 1] == "S" and lines[i + 1][j + 1] == "M")
            ) and (
                #   S
                #  A
                # M
                (lines[i + 1][j - 1] == "M" and lines[i - 1][j + 1] == "S")
                #   M
                #  A
                # S
                or (lines[i + 1][j - 1] == "S" and lines[i - 1][j + 1] == "M")
            ):
                total += 1

    print(total, "OK" if total == 1822 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
