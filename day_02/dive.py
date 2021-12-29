__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def dive_part_1(input_file_path):
    with open(input_file_path) as file:
        directions = file.readlines()

    x, y = 0, 0

    for direction, unit in map(str.split, map(str.strip, directions)):
        match direction:
            case "forward":
                x += int(unit)
            case "down":
                y += int(unit)
            case "up":
                y -= int(unit)

    return x * y


def dive_part_2(input_file_path):
    with open(input_file_path) as file:
        directions = file.readlines()

    x, y, aim = 0, 0, 0

    for direction, unit in map(str.split, map(str.strip, directions)):
        match direction:
            case "forward":
                x += int(unit)
                y += aim * int(unit)
            case "down":
                aim += int(unit)
            case "up":
                aim -= int(unit)

    return x * y


if __name__ == "__main__":
    print(dive_part_1("dive_input.txt"))
    print(dive_part_1("dive_input_sample.txt"))
    print(dive_part_2("dive_input_sample.txt"))
    print(dive_part_2("dive_input.txt"))
