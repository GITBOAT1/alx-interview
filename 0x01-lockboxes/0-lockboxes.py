#!/usr/bin/python3
def canUnlockAll(boxes):
    """number of locked boxes in front of you. Each box is numbered
       sequentially from 0 to n - 1 and each box may contain
       keys to the other boxes.
    """

    # Set of box numbers that are unlocked
    unlocked = {0}
    # List of box numbers that still need to be checked for keys
    to_check = [0]

    while to_check:
        box_num = to_check.pop(0)
        box = boxes[box_num]
        # Check each key in the current box
        for key in box:
            # If the key opens a new box and that box isn't already unlocked
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                to_check.append(key)

    return len(unlocked) == len(boxes)
