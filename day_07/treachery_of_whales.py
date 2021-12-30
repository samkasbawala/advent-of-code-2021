__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def treachery_of_whales_part_1(input_file_path):

    with open(input_file_path) as file:
        positions = [line.strip() for line in file.readlines()]
    positions = [int(pos) for pos in positions[0].split(",")]

    min_fuel = float("inf")
    for pos in range(min(positions), max(positions)):
        fuel = sum(map(lambda x: abs(pos - x), positions))
        min_fuel = fuel if fuel < min_fuel else min_fuel

    return min_fuel


def treachery_of_whales_part_2(input_file_path):

    with open(input_file_path) as file:
        positions = [line.strip() for line in file.readlines()]
    positions = [int(pos) for pos in positions[0].split(",")]

    min_fuel = float("inf")
    for pos in range(min(positions), max(positions)):
        fuel = sum(map(lambda x: int(abs(pos - x) * (abs(pos - x) + 1) / 2), positions))
        min_fuel = fuel if fuel < min_fuel else min_fuel

    return min_fuel


if __name__ == "__main__":
    print(f"Fuel needed: {treachery_of_whales_part_1('input_sample.txt')}")
    print(f"Fuel needed: {treachery_of_whales_part_1('input.txt')}")
    print(f"Fuel needed: {treachery_of_whales_part_2('input_sample.txt')}")
    print(f"Fuel needed: {treachery_of_whales_part_2('input.txt')}")
