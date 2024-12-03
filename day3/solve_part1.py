#!/usr/bin/env python3

import functools
import sys

import enum


class State(enum.Enum):
    NONE = 0  # Initial state while searching for new command
    FUNC_NAME = 1  # While parsing a function name
    PARAMETERS = 2  # mul(X,y)
    SECOND_PARAM = 3  # mul(x,Y)


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    state = State.NONE
    func_name: list[str] = []
    param1: list[str] = []
    param2: list[str] = []
    total = 0

    # Iterate lines
    for line in input_lines:
        # Iterate character by character
        for char in line:

            # Check current state
            match state:
                # Try to find new function
                case State.NONE:
                    # Clear state
                    func_name = []
                    param1 = []
                    param2 = []

                    # Check if we are starting a new function
                    if char == "m":
                        func_name.append(char)
                        state = State.FUNC_NAME
                # Parse function name
                case State.FUNC_NAME:
                    # If function name is in allowed character, append it
                    if char in ["u", "l"]:
                        func_name.append(char)
                    # Checks this parameters start
                    elif char == "(":
                        state = State.PARAMETERS
                    # Otherwise, start over
                    else:
                        state = State.NONE
                # Parse parameters
                case State.PARAMETERS:
                    # Parse function name
                    func_name_str = "".join(func_name)

                    # Check if this is mul(x,y)
                    # Every call (such as mmul(), foomul()) ending with mul is considered a mul call
                    if func_name_str.endswith("mul"):
                        # parse first parameter (x)
                        if char.isdigit():
                            param1.append(char)
                            continue

                        # when comma is found, jump to parsing y. x must have length, mul(,y) is not allowed
                        if char == "," and len(param1):
                            state = State.SECOND_PARAM
                            continue

                        # ignore otherwise
                        state = State.NONE
                    # ignore otherwise
                    else:
                        state = State.NONE
                case State.SECOND_PARAM:
                    # mul(x, y) continues

                    # y can be more than one digit, parse while digit is found
                    if char.isdigit():
                        param2.append(char)
                        continue

                    # when closing parenthesis is found, calculate the mul(x, y). y must have length, mul(x,) is not allowed
                    if char == ")" and len(param2):
                        # parse digits, multiply them and add to total
                        # for example, mul(11, 124) has param1 = [1, 1] and param2 = [1,2,4]
                        total += int("".join(param1)) * int("".join(param2))

                    state = State.NONE

    print(total, "OK" if total == 187194524 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
