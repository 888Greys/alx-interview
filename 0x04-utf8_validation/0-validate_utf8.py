#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need
to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    expected_continuation_bytes = 0

    # Define the UTF-8 bitmasks
    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    # Iterate through each byte in the data
    for byte in data:
        # If the byte is not a valid 8-bit integer, the sequence is invalid
        leading_one_mask = 1 << 7

        # If we are not expecting continuation bytes
        if expected_continuation_bytes == 0:
            # Count the number of leading ones in the byte
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1

            # If the byte is a single byte character, continue
            if expected_continuation_bytes == 0:
                continue

            # If the byte is a multi-byte character, check if it is valid


            # A multi-byte character can start with a "110" prefix
            if expected_continuation_bytes == 1 or\
                    expected_continuation_bytes > 4:
                return False

        # If we are expecting continuation bytes
        else:
            # Check that the byte starts with a "10"
            # prefix and not a "11" prefix
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        # We have found a continuation byte
        expected_continuation_bytes -= 1

    # If we are not expecting any continuation bytes, the sequence is valid
    if expected_continuation_bytes == 0:
        return True
    else:
        return False
