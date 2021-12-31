__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"

import math


def get_floor_map(input_file_path):
    with open(input_file_path) as file:
        floor_map = [line.strip() for line in file.readlines()]

    return [list(string) for string in floor_map]


def get_basins(floor_map):

    basins = []
    for i in range(len(floor_map)):
        for j in range(len(floor_map[i])):

            height = int(floor_map[i][j])

            # True be default if at top row
            up = True if (i == 0 or height < int(floor_map[i - 1][j])) else False

            # True by default if at bottom row
            down = (
                True
                if (i == len(floor_map) - 1 or height < int(floor_map[i + 1][j]))
                else False
            )

            # True by deafult if at left most column
            left = True if (j == 0 or height < int(floor_map[i][j - 1])) else False

            # True by default if at right most column
            right = (
                True
                if (j == len(floor_map[i]) - 1 or height < int(floor_map[i][j + 1]))
                else False
            )

            # If all true, note height and position
            if up and down and left and right:
                basins.append((i, j, height))

    return basins


def get_basin_size(floor_map, i, j):

    try:
        height = int(floor_map[i][j])
    except IndexError:
        return 0

    # Negative indexing works in python, make sure to not process these cases
    if height >= 9 or i < 0 or j < 0:
        return 0

    # Mark that we have been here
    floor_map[i][j] = "9"

    return (
        1
        + get_basin_size(floor_map, i - 1, j)
        + get_basin_size(floor_map, i + 1, j)
        + get_basin_size(floor_map, i, j + 1)
        + get_basin_size(floor_map, i, j - 1)
    )


def smoke_basin_part_1(input_file_path):
    floor_map = get_floor_map(input_file_path)
    basins = get_basins(floor_map)

    return sum([height + 1 for _, _, height in basins])


def smoke_basin_part_2(input_file_path):
    floor_map = get_floor_map(input_file_path)
    basins = get_basins(floor_map)
    basin_sizes = [get_basin_size(floor_map, i, j) for i, j, _ in basins]

    return math.prod(sorted(basin_sizes, reverse=True)[0 : min(3, len(basins))])


if __name__ == "__main__":
    print(f"Sum of risk level: {smoke_basin_part_1('input_sample.txt')}")
    print(f"Sum of risk level: {smoke_basin_part_1('input.txt')}")
    print(f"3 largest basins multiplied: {smoke_basin_part_2('input_sample.txt')}")
    print(f"3 largest basins multiplied: {smoke_basin_part_2('input.txt')}")
