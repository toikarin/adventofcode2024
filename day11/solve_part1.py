#!/usr/bin/env python3

import sys


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    # Strip newlines
    lines = [x.strip() for x in input_lines]
    # Take the first and only line. numerical values are split by space
    line = list(map(int, lines[0].split()))

    # Blink 25 times
    for _ in range(25):
        # Iterate each stone
        stone_idx = 0
        while stone_idx < len(line):
            # Take the current stone
            stone = line[stone_idx]

            if stone == 0:
                # Replace 0 with 1
                line[stone_idx] = 1
            elif len(str(stone)) % 2 == 0:
                # When length of stone digits is even, replace with two stones
                stone_str = str(stone)
                middle = int(len(stone_str) / 2)
                stone1, stone2 = int(stone_str[:middle]), int(stone_str[middle:])

                # Replace current stone with the second stone
                line[stone_idx] = stone2
                # Insert first stone before the second stone
                line.insert(stone_idx, stone1)

                # One extra stone added, skip it
                stone_idx += 1
            else:
                # Otherwise, multiply by 2024
                line[stone_idx] *= 2024

            stone_idx += 1

    # Calculate the number of stones
    total = len(line)
    print(total, "OK" if total == 187738 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
