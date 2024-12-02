#!/usr/bin/env python3

import functools
import sys


def safe(lst: list[int]) -> bool:
    # Sanity check for the list length, never happens
    if len(lst) < 2:
        return True

    prev_diff = None
    for i in range(len(lst) - 1):
        # Calculate the difference
        diff = lst[i] - lst[i + 1]

        # Verify absolute difference is between 1 to 3
        if not (1 <= abs(diff) <= 3):
            return False

        # Check the order is the same as before (diff is always either negative or positive)
        if prev_diff is not None and ((prev_diff < 0) is not (diff < 0)):
            return False

        # Keep track of the last diff
        prev_diff = diff

    # Line is safe
    return True


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    count = 0

    # Iterate lines
    for line in input_lines:
        split_line = list(map(int, line.split()))

        # Increase the count if line is safe
        if safe(split_line):
            count += 1

    print(count, "OK" if count == 326 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
