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
                # Calculate the difference between current frequency position to another position
                diff = (
                    freq_positions[idx][0] - freq_positions[next_idx][0],
                    freq_positions[idx][1] - freq_positions[next_idx][1],
                )

                # Calculate the antinode positions
                first = (
                    freq_positions[idx][0] + diff[0],
                    freq_positions[idx][1] + diff[1],
                )
                second = (
                    freq_positions[next_idx][0] - diff[0],
                    freq_positions[next_idx][1] - diff[1],
                )

                # Verify positions are within the map, if so then new antinode is found
                if 0 <= first[0] < len(lines[0]) and 0 <= first[1] < len(lines):
                    antinodes.add(first)
                if 0 <= second[0] < len(lines[0]) and 0 <= second[1] < len(lines):
                    antinodes.add(second)

    total = len(antinodes)
    print(total, "OK" if total == 320 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
