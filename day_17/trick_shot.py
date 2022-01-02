from __future__ import annotations

__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"

import re


def get_target_area(input_file_path: str) -> set[tuple[int, int]]:
    with open(input_file_path) as file:
        line = file.readline().strip()

    line = line.removeprefix("target area:")
    x_range, y_range = [value.strip() for value in line.split(",")]

    min_x = int(re.search("(?<=^x=)(\\d+)(?=..\\d+)", x_range)[0])
    max_x = int(re.search(f"(?<=^x={min_x}..)(\\d+)", x_range)[0])
    min_y = int(re.search("(?<=^y=)(-*\\d+)(?=..-*\\d+)", y_range)[0])
    max_y = int(re.search(f"(?<=^y={min_y}..)(-*\\d+)", y_range)[0])

    coords = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            coords.add((x, y))

    return coords


def get_highest_y(target_area: set[tuple[int, int]]) -> int:

    # Assumption that lowest_y is always negative
    # Takes 2(y_velo) + 1 time units  to get back to height of 0
    # From 0 to lowest_y is the biggest jump you can make and still be in the zone
    #   Suppose distance from 0 to lowest_y is n, then highest the initial exit velo had
    #   to have been n - 1
    # Highest altitude is a sum from 1 to y_velo = y_velo(y_velo + 1) / 2

    lowest_y = min([y for _, y in target_area])

    y_velo = abs(lowest_y) - 1
    return int(y_velo * (y_velo + 1) / 2)


def get_possible_trajectories(target_area: set[tuple[int, int]]) -> tuple[int, int]:

    # Assumption: target area x_range is always positive, target area y_range is always
    # negative
    longest_x = max([x for x, _ in target_area])
    shortest_x = min([x for x, _ in target_area])
    lowest_y = min([y for _, y in target_area])

    x_velo_min = get_x_velo_min(shortest_x)
    x_velo_max = longest_x
    y_velo_min = lowest_y
    y_velo_max = abs(lowest_y) - 1

    valid = set()
    for x in range(x_velo_min, x_velo_max + 1):
        for y in range(y_velo_min, y_velo_max + 1):
            if valid_velos(x, y, target_area):
                valid.add((x, y))

    return valid


def get_x_velo_min(shortest_x: int) -> int:

    # Assumption: target area x_range is always positive, target area y_range is always
    # negative
    x_velo = 0
    x_distance = int(x_velo * (x_velo + 1) / 2)
    while x_distance < shortest_x:
        if shortest_x <= x_distance:
            break
        x_velo += 1
        x_distance = int(x_velo * (x_velo + 1) / 2)

    return x_velo


def valid_velos(x_velo: int, y_velo: int, target_area: set[tuple[int, int]]) -> bool:

    # Assumption: target area x_range is always positive, target area y_range is always
    # negative
    longest_x = max([x for x, _ in target_area])
    lowest_y = min([y for _, y in target_area])

    x_pos, y_pos = 0, 0
    step = 0
    x_pos = x_velo - step
    y_pos = y_velo - step

    while x_pos <= longest_x and y_pos >= lowest_y:
        if (x_pos, y_pos) in target_area:
            return True
        step += 1
        x_pos = x_pos + max(0, x_velo - step)
        y_pos = y_pos + (y_velo - step)

    return False


if __name__ == "__main__":
    assert get_highest_y(get_target_area("input_sample.txt")) == 45
    print(get_highest_y(get_target_area("input.txt")))

    assert len(get_possible_trajectories(get_target_area("input_sample.txt"))) == 112
    print(len(get_possible_trajectories(get_target_area("input.txt"))))
