#!/usr/bin/env python3

import collections
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

    # Calculate the number of occurances of each element in second list
    counted_list = collections.Counter(second_list)

    # Calculate the similarity score for each element in first list
    # Similarity score: <value> * number of occurances in the counted list
    similarities = map(lambda i: i * counted_list[i], first_list)
    # Calculate total similarity
    similarity = functools.reduce(lambda a, b: a + b, similarities)

    # Print the solution
    print(similarity, "OK" if 21607792 == similarity else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
