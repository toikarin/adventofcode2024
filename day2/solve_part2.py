#!/usr/bin/env python3

import functools
import sys


def safe_by_removing_one_element(lst: list[int]) -> bool:
    # Brute-force check if removing one element from the list produces a safe list
    for i in range(len(lst)):
        # Create copy of the original list
        list_without_index = lst[:]
        # Remove one element
        del list_without_index[i]
        # Check if that list is safe
        if safe(list_without_index, False):
            return True

    return False


def safe(lst: list[int], allow_adjust: bool = True) -> bool:
    # Sanity check for the list length, never happens
    if len(lst) < 2:
        return True

    prev_diff = None
    for i in range(len(lst) - 1):
        # Calculate the difference
        diff = lst[i] - lst[i + 1]

        # Verify absolute difference is between 1 to 3
        if not (1 <= abs(diff) <= 3):
            if allow_adjust:
                return safe_by_removing_one_element(lst)

            return False

        # Check the order is the same as before (diff is always either negative or positive)
        if prev_diff is not None and ((prev_diff < 0) is not (diff < 0)):
            if allow_adjust:
                return safe_by_removing_one_element(lst)

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

    print(count, "OK" if count == 381 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
