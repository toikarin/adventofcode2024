#!/usr/bin/env python3

import sys
from collections import defaultdict


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    # Strip newlines
    lines = [x.strip() for x in input_lines]

    positions = defaultdict(list)
    # Iterate lines
    for i, line in enumerate(lines):
        # Iterate characters
        for j, frequency in enumerate(line):
            # Skip positions without nodes
            if not frequency.isalnum():
                continue

            # Add this position to the list of current positions for this frequency
            positions[frequency].append((i, j))

    # Unique positions for antinodes
    antinodes = set()

    # Iterate all frequencies
    for _, freq_positions in positions.items():
        # Iterate all positions for this frequency
        for idx, cur_pos in enumerate(freq_positions):
            # Loop rest of the frequency values
            for next_idx in range(idx + 1, len(freq_positions)):
                # Add antinodes at frequency positions
                antinodes.add(freq_positions[idx])
                antinodes.add(freq_positions[next_idx])

                # Calculate the difference between current frequency position to another position
                diff = (
                    freq_positions[idx][0] - freq_positions[next_idx][0],
                    freq_positions[idx][1] - freq_positions[next_idx][1],
                )

                def find_positions(p: tuple[int, int], plus: bool):
                    retval = set()
                    factor = 1 if plus else -1

                    # Find until out of bounds
                    while True:
                        # Calculate the next point
                        p = ((p[0] + factor * diff[0]), (p[1] + factor * diff[1]))

                        if 0 <= p[0] < len(lines[0]) and 0 <= p[1] < len(lines):
                            # If position is valid, add to the list of found positions
                            retval.add(p)
                        else:
                            # If not valid, break the loop and return
                            break

                    return retval

                # Find all antinode positions for these to frequencies
                antinodes.update(find_positions(freq_positions[idx], True))
                antinodes.update(find_positions(freq_positions[next_idx], False))

    total = len(antinodes)
    print(total, "OK" if total == 1157 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
