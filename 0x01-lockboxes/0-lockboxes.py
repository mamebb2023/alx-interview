#!/usr/bin/python3
""" LockBoxes """


def canUnlockAll(boxes):
    """ Can all the boxes be unlocked? """
    keys = set()
    opened = []
    i = 0

    while i < len(boxes):
        temp = i
        opened.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < len(boxes) and key not in opened:
                i = key
                break
        if temp == i:
            break

    for i in range(len(boxes)):
        if i not in opened:
            return False
    return True
