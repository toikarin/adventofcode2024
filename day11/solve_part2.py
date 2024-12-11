#!/usr/bin/env python3

import sys
from collections import defaultdict


cache: dict[int, dict[int, int]] = defaultdict(dict)


def calculate_stone(stone: int, blinks_left: int) -> int:
    # Stop calculating when there's no blinks left,
    # each stone has value value of 1
    if blinks_left == 0:
        return 1

    # First, check from cache if we have calculated already with this value/blinks
    val = cache[blinks_left].get(stone, None)
    if val is not None:
        return val

    # Not found from cache, continue to calculate
    if stone == 0:
        # Replace 0 with 1
        val = calculate_stone(1, blinks_left - 1)
    elif len(str(stone)) % 2 == 0:
        # When length of stone digits is even, replace with two stones
        stone_str = str(stone)
        middle = int(len(stone_str) / 2)
        stone1, stone2 = int(stone_str[:middle]), int(stone_str[middle:])

        val = calculate_stone(stone1, blinks_left - 1) + calculate_stone(
            stone2, blinks_left - 1
        )
    else:
        # Otherwise, multiply by 2024
        val = calculate_stone(stone * 2024, blinks_left - 1)

    # Cache the result
    cache[blinks_left][stone] = val

    # Return calculated result
    return val


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    # Strip newlines
    lines = [x.strip() for x in input_lines]

    total = 0
    # Iterate each stone
    for stone in lines[0].split():
        # Calculate how many stones this stone will be
        # replaced by end of 75 blinks. Add that to total
        total += calculate_stone(int(stone), 75)

    print(total, "OK" if total == 223767210249237 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
