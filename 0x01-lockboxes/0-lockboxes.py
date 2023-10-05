#!/usr/bin/python3

"""number of locked boxes in front of you. Each box is numbered
   sequentially from 0 to n - 1 and each box may
"""


def canUnlockAll(boxes):
    """number of locked boxes in front of you. Each box is numbered
       sequentially from 0 to n - 1 and each box may contain
       keys to the other boxes.
    """

    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes  # set Each element in list to False
    unlocked_boxes[0] = True
    keys = [0]

    while keys:
        box_idx = keys.pop()
        for key in boxes[box_idx]:
            if key < num_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                keys.append(key)
    return all(unlocked_boxes)
