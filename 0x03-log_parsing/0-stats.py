#!/usr/bin/python3
''' Define a function to print the metrics '''

import sys


def print_stats(total_size, status_codes):
    """ Function to print the status code after sorting in ascending order"""
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


def parse_input(line):
    """ Extract the file size and status code from each line of input."""
    try:
        fields = line.split(" ")
        size = int(fields[-1])
        code = int(fields[-2])
        return (size, code)
    except Exception:
        return None


def main():
    """
    Initializes variables used for tracking total file size & num of lines.
    Reads standard input line by line, updates the var accordingly, &
    prints stats every 10 lines &/or when keyboard interruption occurs
    """
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                    500: 0}
    count = 0
    try:
        for line in sys.stdin:
            parsed = parse_input(line)
            if parsed:
                size, code = parsed
                total_size += size
                if code in status_codes:
                    status_codes[code] += 1
                count += 1
            if count % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        # sys.exit(0)
        raise


if __name__ == '__main__':
    main()
