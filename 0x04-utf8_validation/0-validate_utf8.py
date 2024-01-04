#!/usr/bin/env python3
""" UTF8 Validation
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """ Checkes if a given data is a valid UTF8 encoding

    Args:
        data (list[int]): list of ints

    Return: a True if valid or False if otherwise
    """
    count = 0  # Keeping track of bytes
    for byte in data:
        if count == 0:
            # Check the first byte of a character
            if (byte >> 7) == 0:  # 0b0xxxxxxx
                count = 0
            elif (byte >> 5) == 0b110:  # 0b110xxxxx
                count = 1
            elif (byte >> 4) == 0b1110:  # 0b1110xxxx
                count = 2
            elif (byte >> 5) == 0b11110:  # 0b11110xxx
                count = 3
            else:  # Invalid starting byte
                return False
        else:
            # Check subsequent continuation bytes
            if (byte >> 6) != 0b10:  # not 0b10xxxxxx
                return False
            count -= 1

    return count == 0
