# Dec 3 2025
# Python 3.14.0

# Advent of Code 2025
# Day 2: Gift Shop
# https://adventofcode.com/2025/day/2

import time
import re


def main():
    with open("input.txt", encoding="UTF-8") as input_file:
        id_ranges = input_file.read().split(",")

    count = 0
    count2 = 0
    for idr in id_ranges:
        l, r = [int(x) for x in idr.split("-")]
        for num in range(l, r+1):
            if re.match(r"^(\d*)\1$", str(num)):
                count += num
            if re.match(r"^(\d*)\1+$", str(num)):
                count2 += num

    print(f"Part 1: {count}")
    print(f"Part 2: {count2}")


if __name__ == "__main__":
    start_time = time.perf_counter() * 1000
    main()
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
