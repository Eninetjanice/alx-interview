#!/usr/bin/python3
"""Script to determine if given data set represents a valid UTF-8 encoding."""


def validUTF8(data) -> bool:
    """
    UTF-8 validation
    :param data:
    :return True if data == valid UTF-8 encoding, else return False
    """
    i = 0

    # Iterate through each byte in the data set
    while i < len(data):
        byte = data[i]

        # Determine num of bytes needed to form UTF-8 character
        if byte < 0b10000000:
            num_bytes = 1
        elif byte < 0b11100000:
            num_bytes = 2
        elif byte < 0b11110000:
            num_bytes = 3
        elif byte < 0b11111000:
            num_bytes = 4
        else:
            # Invalid UTF-8 character
            return False

        if i + num_bytes > len(data):
            return False

        # Check if the next num_bytes-1 bytes start with the 0b10 prefix
        for j in range(1, num_bytes):
            if data[i+j] >> 6 != 0b10:
                return False

        # Increment index
        i += num_bytes

    return True
