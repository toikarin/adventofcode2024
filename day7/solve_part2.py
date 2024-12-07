#!/usr/bin/env python3

import sys


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    total = 0
    equations = []

    # Strip newlines
    for line in input_lines:
        # Split line tot test value and list of values
        # example line: `292: 11 6 16 20 `
        split = line.strip().split(": ")
        test_value = int(split[0])
        values = list(map(int, split[1].split(" ")))

        sums = []
        for current in range(len(values)):
            # Initially add only the current value
            if not sums:
                sums.append(values[current])
                continue

            # Calculate the new possible sums
            new_sums = []
            for s in sums:
                new_sums.append(s + values[current])
                new_sums.append(s * values[current])
                new_sums.append(int(str(s) + str(values[current])))

            # Replace the sums with the new list
            sums = new_sums

        # Test if test value is found in calculated sums
        if test_value in sums:
            total += test_value

    print(total, "OK" if total == 44841372855953 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
