#!/usr/bin/env python3

import functools
import sys

import enum


class State(enum.Enum):
    NONE = 0  # Initial state while searching for new command
    FUNC_NAME = 1  # While parsing a function name
    PARAMETERS = 2  # mul(X,y), do(), don't()
    SECOND_PARAM = 3  # mul(x,Y)


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    state = State.NONE
    func_name: list[str] = []
    machine_enabled = True
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
                    if char in ["m", "d"]:
                        func_name.append(char)
                        state = State.FUNC_NAME
                # Parse function name
                case State.FUNC_NAME:
                    # If function name is in allowed character, append it
                    if char in ["m", "u", "l", "d", "o", "n", "'", "t"]:
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
                    # Every call (such as mmul(), domul()) ending with mul is considered a mul call
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
                    elif func_name_str.endswith("do") or func_name_str.endswith(
                        "don't"
                    ):
                        # Call must be without parameters
                        if char == ")":
                            # Set machine to enabled / disabled based on the command
                            machine_enabled = func_name_str == "do"

                        # always jump back to nonestate
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
                    # machine must also be enabled.
                    if char == ")" and len(param2) and machine_enabled:
                        # parse digits, multiply them and add to total
                        # for example, mul(11, 124) has param1 = [1, 1] and param2 = [1,2,4]
                        total += int("".join(param1)) * int("".join(param2))

                    state = State.NONE

    print(total, "OK" if total == 127092535 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
