#!/usr/bin/python3
"""
Write a method that determines if a given
data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    # Number of bytes remaining for the current character
    remaining_bytes = 0

    for byte in data:
        # Check if the current byte is a continuation byte
        if remaining_bytes > 0 and (byte & 0b11000000) == 0b10000000:
            remaining_bytes -= 1
        # Check if the current byte is a new character's starting byte
        elif remaining_bytes == 0:
            # Determine the number of bytes for the current character
            if (byte & 0b10000000) == 0:
                # 1-byte character (ASCII)
                remaining_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:
                # 2-byte character
                remaining_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:
                # 3-byte character
                remaining_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:
                # 4-byte character
                remaining_bytes = 3
            else:
                # Invalid starting byte
                return False
        else:
            # Invalid continuation byte
            return False

    """ If there are remaining bytes
    after iterating through the data, it's invalid
    """
    return remaining_bytes == 0
