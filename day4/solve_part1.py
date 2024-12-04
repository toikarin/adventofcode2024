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
            # No need to search unless current char is X
            if char != "X":
                continue

            # Backwards, SAMX
            if (
                j >= 3
                and line[j - 1] == "M"
                and line[j - 2] == "A"
                and line[j - 3] == "S"
            ):
                total += 1
            # Forwards, XMAS
            if (
                j + 3 < len(line)
                and line[j + 1] == "M"
                and line[j + 2] == "A"
                and line[j + 3] == "S"
            ):
                total += 1
            # Up, S
            #     A
            #     M
            #     X
            if (
                i >= 3
                and lines[i - 1][j] == "M"
                and lines[i - 2][j] == "A"
                and lines[i - 3][j] == "S"
            ):
                total += 1
            # Down, X
            #       M
            #       A
            #       S
            if (
                i + 3 < len(lines)
                and lines[i + 1][j] == "M"
                and lines[i + 2][j] == "A"
                and lines[i + 3][j] == "S"
            ):
                total += 1
            # Diagonal, up-left
            # S
            #  A
            #   M
            #    X
            if (
                j >= 3
                and i >= 3
                and lines[i - 1][j - 1] == "M"
                and lines[i - 2][j - 2] == "A"
                and lines[i - 3][j - 3] == "S"
            ):
                total += 1
            # Diagonal, up-right
            #    S
            #   A
            #  M
            # X
            if (
                j + 3 < len(line)
                and i >= 3
                and lines[i - 1][j + 1] == "M"
                and lines[i - 2][j + 2] == "A"
                and lines[i - 3][j + 3] == "S"
            ):
                total += 1
            # Diagonal, down-left
            #    X
            #   M
            #  A
            # S
            if (
                j >= 3
                and i + 3 < len(lines)
                and lines[i + 1][j - 1] == "M"
                and lines[i + 2][j - 2] == "A"
                and lines[i + 3][j - 3] == "S"
            ):
                total += 1
            # Diagonal, down-right
            # X
            #  M
            #   A
            #    S
            if (
                j + 3 < len(line)
                and i + 3 < len(lines)
                and lines[i + 1][j + 1] == "M"
                and lines[i + 2][j + 2] == "A"
                and lines[i + 3][j + 3] == "S"
            ):
                total += 1

    print(total, "OK" if total == 2401 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
