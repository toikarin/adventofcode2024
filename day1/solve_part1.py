#!/usr/bin/env python3

import functools
import sys


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    # Read lists
    first_list = []
    second_list = []

    for line in input_lines:
        split_line = line.split()

        first_list.append(int(split_line[0]))
        second_list.append(int(split_line[1]))

    # Sort list from smallest to highest
    first_list = sorted(first_list)
    second_list = sorted(second_list)

    # Calculate distances between ordered list elements
    distances = map(lambda i: abs(i[0] - i[1]), zip(first_list, second_list))
    # Calculate total distance
    total_distance = functools.reduce(lambda a, b: a + b, distances)

    # Print the solution
    print(total_distance, "OK" if 1834060 == total_distance else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
