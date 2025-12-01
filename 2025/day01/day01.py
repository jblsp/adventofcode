# Dec 1 2025
# Python 3.14.0

# Advent of Code 2025
# Day 1: Secret Entrance
# https://adventofcode.com/2025/day/1

import time


def main():
    with open("input.txt", encoding="UTF-8") as input_file:
        in_lines = input_file.read().splitlines()

    zero_counter = 0
    zero_counter_2 = 0
    dial_pos = 50
    for line in in_lines:
        d = line[0]
        m = int(line[1:])
        if d == "L":
            if dial_pos == 0:
                zero_counter_2 -= 1
            dial_pos -= m
            if dial_pos <= 0:
                zero_counter_2 += (abs(dial_pos) // 100) + 1
        if d == "R":
            dial_pos += m
            zero_counter_2 += dial_pos // 100
        dial_pos %= 100
        if dial_pos == 0:
            zero_counter += 1

    # Part 1: 1031
    print(f"Part 1: {zero_counter}")

    # Part 2: 5831
    print(f"Part 2: {zero_counter_2}")


if __name__ == "__main__":
    start_time = time.perf_counter() * 1000
    main()
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
