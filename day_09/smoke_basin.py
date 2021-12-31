__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"

import math


def smoke_basin_part_1(input_file_path):

    with open(input_file_path) as file:
        floor_map = [line.strip() for line in file.readlines()]

    sum = 0
    for i in range(len(floor_map)):
        for j in range(len(floor_map[i])):

            height = int(floor_map[i][j])

            # Top left
            if i == 0 and j == 0:
                if height < int(floor_map[i + 1][j]) and height < int(
                    floor_map[i][j + 1]
                ):
                    sum += height + 1

            # Top right
            elif i == 0 and j == len(floor_map[i]) - 1:
                if height < int(floor_map[i + 1][j]) and height < int(
                    floor_map[i][j - 1]
                ):
                    sum += height + 1

            # Bottom left
            elif i == len(floor_map) - 1 and j == 0:
                if height < int(floor_map[i - 1][j]) and height < int(
                    floor_map[i][j + 1]
                ):
                    sum += height + 1

            # Bottom right
            elif i == len(floor_map) - 1 and j == len(floor_map[i]) - 1:
                if height < int(floor_map[i - 1][j]) and height < int(
                    floor_map[i][j - 1]
                ):
                    sum += height + 1

            # Top row
            elif i == 0:
                if (
                    height < int(floor_map[i + 1][j])
                    and height < int(floor_map[i][j - 1])
                    and height < int(floor_map[i][j + 1])
                ):
                    sum += height + 1

            # Bottom row
            elif i == len(floor_map) - 1:
                if (
                    height < int(floor_map[i - 1][j])
                    and height < int(floor_map[i][j - 1])
                    and height < int(floor_map[i][j + 1])
                ):
                    sum += height + 1

            # Left edge
            elif j == 0:
                if (
                    height < int(floor_map[i][j + 1])
                    and height < int(floor_map[i + 1][j])
                    and height < int(floor_map[i - 1][j])
                ):
                    sum += height + 1

            # Right edge
            elif j == len(floor_map[i]) - 1:
                if (
                    height < int(floor_map[i][j - 1])
                    and height < int(floor_map[i + 1][j])
                    and height < int(floor_map[i - 1][j])
                ):
                    sum += height + 1

            # Four adjacent spots
            else:
                if (
                    height < int(floor_map[i][j + 1])
                    and height < int(floor_map[i][j - 1])
                    and height < int(floor_map[i + 1][j])
                    and height < int(floor_map[i - 1][j])
                ):
                    sum += height + 1

    return sum


def get_basin_size(floor_map, i, j):

    height = int(floor_map[i][j])

    if height >= 9:
        return 0

    # Mark that we have been here
    tmp = list(floor_map[i])
    tmp[j] = "9"
    floor_map[i] = "".join(tmp)

    # Top left
    if i == 0 and j == 0:
        return (
            1
            + get_basin_size(floor_map, i, j + 1)
            + get_basin_size(floor_map, i + 1, j)
        )

    # Top right
    elif i == 0 and j == len(floor_map[i]) - 1:
        return (
            1
            + get_basin_size(floor_map, i, j - 1)
            + get_basin_size(floor_map, i + 1, j)
        )

    # Bottom left
    elif i == len(floor_map) - 1 and j == 0:
        return (
            1
            + get_basin_size(floor_map, i - 1, j)
            + get_basin_size(floor_map, i, j + 1)
        )

    # Bottom right
    elif i == len(floor_map) - 1 and j == len(floor_map[i]) - 1:
        return (
            1
            + get_basin_size(floor_map, i - 1, j)
            + get_basin_size(floor_map, i, j - 1)
        )

    # Top row
    elif i == 0:
        return (
            1
            + get_basin_size(floor_map, i, j - 1)
            + get_basin_size(floor_map, i, j + 1)
            + get_basin_size(floor_map, i + 1, j)
        )

    # Bottom row
    elif i == len(floor_map) - 1:
        return (
            1
            + get_basin_size(floor_map, i, j - 1)
            + get_basin_size(floor_map, i, j + 1)
            + get_basin_size(floor_map, i - 1, j)
        )

    # Left edge
    elif j == 0:
        return (
            1
            + get_basin_size(floor_map, i - 1, j)
            + get_basin_size(floor_map, i + 1, j)
            + get_basin_size(floor_map, i, j + 1)
        )

    # Right edge
    elif j == len(floor_map[i]) - 1:
        return (
            1
            + get_basin_size(floor_map, i - 1, j)
            + get_basin_size(floor_map, i + 1, j)
            + get_basin_size(floor_map, i, j - 1)
        )

    # Four adjacent spots
    else:
        return (
            1
            + get_basin_size(floor_map, i - 1, j)
            + get_basin_size(floor_map, i + 1, j)
            + get_basin_size(floor_map, i, j + 1)
            + get_basin_size(floor_map, i, j - 1)
        )


def smoke_basin_part_2(input_file_path):

    with open(input_file_path) as file:
        floor_map = [line.strip() for line in file.readlines()]

    basins = []
    for i in range(len(floor_map)):
        for j in range(len(floor_map[i])):

            height = int(floor_map[i][j])

            # Top left
            if i == 0 and j == 0:
                if height < int(floor_map[i + 1][j]) and height < int(
                    floor_map[i][j + 1]
                ):
                    basins.append(get_basin_size(floor_map, i, j))

            # Top right
            elif i == 0 and j == len(floor_map[i]) - 1:
                if height < int(floor_map[i + 1][j]) and height < int(
                    floor_map[i][j - 1]
                ):
                    basins.append(get_basin_size(floor_map, i, j))

            # Bottom left
            elif i == len(floor_map) - 1 and j == 0:
                if height < int(floor_map[i - 1][j]) and height < int(
                    floor_map[i][j + 1]
                ):
                    basins.append(get_basin_size(floor_map, i, j))

            # Bottom right
            elif i == len(floor_map) - 1 and j == len(floor_map[i]) - 1:
                if height < int(floor_map[i - 1][j]) and height < int(
                    floor_map[i][j - 1]
                ):
                    basins.append(get_basin_size(floor_map, i, j))

            # Top row
            elif i == 0:
                if (
                    height < int(floor_map[i + 1][j])
                    and height < int(floor_map[i][j - 1])
                    and height < int(floor_map[i][j + 1])
                ):
                    basins.append(get_basin_size(floor_map, i, j))

            # Bottom row
            elif i == len(floor_map) - 1:
                if (
                    height < int(floor_map[i - 1][j])
                    and height < int(floor_map[i][j - 1])
                    and height < int(floor_map[i][j + 1])
                ):
                    basins.append(get_basin_size(floor_map, i, j))

            # Left edge
            elif j == 0:
                if (
                    height < int(floor_map[i][j + 1])
                    and height < int(floor_map[i + 1][j])
                    and height < int(floor_map[i - 1][j])
                ):
                    basins.append(get_basin_size(floor_map, i, j))

            # Right edge
            elif j == len(floor_map[i]) - 1:
                if (
                    height < int(floor_map[i][j - 1])
                    and height < int(floor_map[i + 1][j])
                    and height < int(floor_map[i - 1][j])
                ):
                    basins.append(get_basin_size(floor_map, i, j))

            # Four adjacent spots
            else:
                if (
                    height < int(floor_map[i][j + 1])
                    and height < int(floor_map[i][j - 1])
                    and height < int(floor_map[i + 1][j])
                    and height < int(floor_map[i - 1][j])
                ):
                    basins.append(get_basin_size(floor_map, i, j))

    return math.prod(sorted(basins, reverse=True)[0 : min(3, len(basins))])


if __name__ == "__main__":
    print(f"Sum of risk level: {smoke_basin_part_1('input_sample.txt')}")
    print(f"Sum of risk level: {smoke_basin_part_1('input.txt')}")
    print(f"Sum of risk level: {smoke_basin_part_2('input_sample.txt')}")
    print(f"Sum of risk level: {smoke_basin_part_2('input.txt')}")
