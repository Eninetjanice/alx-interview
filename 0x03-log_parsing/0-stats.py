#!/usr/bin/python3
''' Define a function to print the metrics '''

from sys import stdin


def parse_input(line):
    """ Extract the file size and status code from each line of input."""
    fields = line.split()
    if len(fields) < 7:
        return None
    try:
        size = int(fields[-1])
        status_code = int(fields[-2])
        return (size, status_code)
    except ValueError:
        return None


def print_stats(total_size, status_codes):
    """ Function to print the status code after sorting in ascending order"""
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] > 0:
            print("{}: {}".format(key, status_codes[key]))


def main():
    """
    Initializes variables used for tracking total file size & num of lines.
    Reads standard input line by line, updates the var accordingly, &
    prints stats every 10 lines &/or when keyboard interruption occurs
    """
    line_num = 0
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in stdin:
            line_num += 1
            parsed = parse_input(line)
            if parsed:
                size, status_code = parsed
                total_size += size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_num % 10 == 0:
                print_stats(total_size, status_codes)

        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        # sys.exit(0)
        raise


if __name__ == '__main__':
    main()
