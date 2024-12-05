#!/usr/bin/env python3

import sys


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    # Strip newlines
    lines = [x.strip() for x in input_lines]

    still_parsing_rules = True
    page_ordering_rules = []
    pages_to_produce = []

    # Iterate lines
    for line in lines:
        # Use empty space to separate which part are we parsing
        if not line:
            still_parsing_rules = False
            continue

        # are we still parsing rules?
        if still_parsing_rules:
            # Rules are in format x|y, page x must be before y
            split = line.split("|")
            page_ordering_rules.append((int(split[0]), int(split[1])))
        else:
            # Pages list is a comma separated list of pages
            pages_to_produce.append(list(map(int, line.split(","))))

    total = 0

    # Iterate the pages
    for page in pages_to_produce:
        # Did this page have error?
        page_had_error = False

        # Iterate until all errors has been corrected
        while True:
            # Has error found in this iteration?
            error_corrected = False

            # Iterate rules
            for rule in page_ordering_rules:
                try:
                    # Check if page is OK
                    index1 = page.index(rule[0])
                    index2 = page.index(rule[1])
                    page_ok = index1 < index2

                    if not page_ok:
                        # Page is not OK, make it more correct
                        page[index1], page[index2] = rule[1], rule[0]
                        error_corrected = True
                        page_had_error = True
                except ValueError:
                    # If one or more pages are not in list, ignore the rule
                    pass

            # When no more errors have been corrected, no more error correction needed
            if not error_corrected:
                break

        # Calculate the total value of middle elements of the page that HAD errors
        if page_had_error:
            middle = page[int(len(page) / 2)]
            total += middle

    print(total, "OK" if total == 5017 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
