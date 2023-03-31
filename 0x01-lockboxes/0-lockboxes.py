#!/usr/bin/python3

"""
This implements a simple algorithm to determine if all boxes in a list of lists can be opened using keys contained in other boxes. The function returns True if all boxes can be opened and False if otherwise.
"""
def canUnlockAll(boxes):
    """ Function to determine if all boxes can be opened """
    # Initialize the list of unlocked boxes with box 0
    unlocked = [0]

    # Iterate over each box and its contents
    for box_id, box in enumerate(boxes):
        # If not box, skip to the next one
        if not box:
            continue

        # Iterate over each key in the box
        for key in box:
             # If key unlocks an unlocked box && isn't the current box,
             # append to the list of unlocked boxes
            if key < len(boxes) and key not in unlocked and key != box_id:
                unlocked.append(key)

    # If num of unlocked boxes == total num of boxes, return True, else return false
    if len(unlocked) == len(boxes):
        return True
    return False
