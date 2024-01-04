#!/usr/bin/python3
""" UTF-8 validation
"""
from typing import List


def validUTF8(data):
    """ Checkes if a given data is a valid UTF-8
    Args:
        data (list): list of ints
    Return:
        True if valid and False if other wise
    """
    count = 0
    for byte in data:
        byte &= 0xFF

        if count == 0:
            if byte < 0x80:  # Single-byte
                count = 0
            elif byte < 0xC2:  # Invalid start byte
                return False
            elif byte < 0xE0:  # Two-byte char
                count = 1
            elif byte < 0xF0:  # Three-byte char
                count = 2
            elif byte < 0xF8:  # Four-byte char
                count = 3
            else:  # Invalid start byte
                return False
        else:
            # Check continuation byte
            if byte < 0x80 or byte > 0xBF:  # Invalid continuation bute
                return False
            count -= 1

    return count == 0
