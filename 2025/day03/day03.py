# Dec 7 2025
# Python 3.14.0

# Advent of Code 2025
# Day 3: Lobby
# https://adventofcode.com/2025/day/3

import time


def solve(pinput, num_digits):
    banks = pinput.splitlines()
    res = 0
    for bank in banks:
        bl = len(bank)
        digits = [0] * num_digits
        digits[0] = int(bank[0])
        for i, bat in enumerate(bank[1:]):
            bat = int(bat)
            for k in range(num_digits - min(bl - i - 1, num_digits), num_digits):
                if bat > digits[k]:
                    digits[k] = bat
                    digits[k + 1 :] = [0] * (num_digits - (k + 1))
                    break
        for i, digit in enumerate(digits):
            res += digit * (10 ** (num_digits - i - 1))
    return res


if __name__ == "__main__":
    with open("input.txt", encoding="UTF-8") as input_file:
        pinput = input_file.read()
    start_time = time.perf_counter() * 1000
    print(f"Part 1: {solve(pinput, 2)}")
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds\n")
    print(f"Part 2: {solve(pinput, 12)}")
    end_time = time.perf_counter() * 1000
    print(f"Execution time: {round(end_time - start_time, 3)} milliseconds")
