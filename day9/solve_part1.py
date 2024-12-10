#!/usr/bin/env python3

import sys


def solve(filename: str) -> None:
    # Read the input file
    with open(filename, "r") as f:
        input_lines = f.readlines()

    # Strip newlines
    lines = [x.strip() for x in input_lines]

    # Single line is needed
    line = lines[0]

    current_id = 0
    blocks = []
    block_is_free = False

    # Iterate characters, create a list of blocks
    for char in line:
        blocks.append({ "index": current_id if not block_is_free else None, "length": int(char), "is_free": block_is_free})
        if not block_is_free:
            current_id += 1
        block_is_free = not block_is_free

    # Iterate blocks from right to left, try to move them to free space
    done = False
    block_to_move_index = len(blocks) - 1
    while block_to_move_index >= 0 and not done:
        block_to_move = blocks[block_to_move_index]

        # Skip free blocks
        if block_to_move["is_free"]:
            block_to_move_index -= 1
            continue

        free_space_needed = block_to_move["length"]

        # Iterate available blocks from left-to-right
        for i, free_block in enumerate(blocks):
            # If we are already looking beyond the current move to block,
            # it's time to quit
            if i >= block_to_move_index:
                done = True
                break

            # Ignore non-free blocks
            if not free_block["is_free"]:
                continue

            # If we found an exact match, just replace the blocks
            if free_block["length"] == free_space_needed:
                # Replace blocks
                blocks[block_to_move_index] = blocks[i]
                blocks[i] = block_to_move

                # We are done, fully replaced
                block_to_move_index -= 1
                break
            # If we found more than enough space, replace the blocks and add a new free block
            elif free_block["length"] > free_space_needed:
                diff = free_block["length"] - free_space_needed

                # 1. Move block over the free block
                blocks[i] = block_to_move

                # 2. Create new free block after the moved block
                blocks.insert(i + 1, { "index": None, "length": diff, "is_free": True})

                # 3. Create new free block, +1 because we just inserted one
                blocks[block_to_move_index + 1] = { "index": None, "length": block_to_move["length"], "is_free": True}

                break
            else:
                # Take what we can
                blocks[i] = { "index": block_to_move["index"], "length": free_block["length"], "is_free": False }

                # Replace the currently moved block with one with a smaller length
                block_to_move = { "index": block_to_move["index"], "length": block_to_move["length"] - free_block["length"], "is_free": False}
                blocks[block_to_move_index] = block_to_move

                # Create new free block after the block
                blocks.insert(block_to_move_index + 1, { "index": None, "length": free_block["length"], "is_free": True})

                free_space_needed -= free_block["length"]

    # Calculate checksum
    total = 0
    i = 0
    for block in blocks:
        if block["is_free"]:
            # Skip free blocks
            i += block["length"]
        else:
            # Add the block's index multiplied with the location to the checksum
            for _ in range(block["length"]):
                total += i * block["index"]
                i += 1

    print(total, "OK" if total == 6471961544878 else "NOK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input-file>")
        exit(1)

    solve(sys.argv[1])
