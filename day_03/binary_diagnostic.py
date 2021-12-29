__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def binary_diagnostic_part_1(input_file_path):
    with open(input_file_path) as file:
        report = file.readlines()

    num_readings = len(report)
    count = dict()

    # Count number of ones at each index
    for reading in map(str.strip, report):
        for index, bit in enumerate(reading):
            if int(bit) == 1:
                count[index] = count.get(index, 0) + 1

    gamma = ""
    epsilon = ""
    for k, v in sorted(count.items(), key=lambda x: x[0]):
        if (v / num_readings) < (1 / 2):
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


def binary_diagnostic_part_2(input_file_path):
    with open(input_file_path) as file:
        report = [_ for _ in map(str.strip, file.readlines())]

    # Get oxygen reading
    index = 0
    oxygen_rating = report
    while len(oxygen_rating) > 1:

        # How many ones in the current index position
        total = sum([1 for reading in oxygen_rating if reading[index] == "1"])

        # Keep readings with most common bit at current index
        if total < (len(oxygen_rating) / 2):
            oxygen_rating = [
                reading for reading in oxygen_rating if reading[index] == "0"
            ]
        else:
            oxygen_rating = [
                reading for reading in oxygen_rating if reading[index] == "1"
            ]
        index += 1

    # Get CO2 reading
    index = 0
    C02_rating = report
    while len(C02_rating) > 1:

        # How many ones in the current index position
        total = sum([1 for reading in C02_rating if reading[index] == "1"])

        # Keep readings with least common bit at current index
        if total < (len(C02_rating) / 2):
            C02_rating = [reading for reading in C02_rating if reading[index] == "1"]
        else:
            C02_rating = [reading for reading in C02_rating if reading[index] == "0"]
        index += 1

    return int(oxygen_rating[0], 2) * int(C02_rating[0], 2)


if __name__ == "__main__":
    print(f"Power Consumption: {binary_diagnostic_part_1('input_sample.txt')}")
    print(f"Power Consumption: {binary_diagnostic_part_1('input.txt')}")
    print(f"Life Support Rating: {binary_diagnostic_part_2('input_sample.txt')}")
    print(f"Life Support Rating: {binary_diagnostic_part_2('input.txt')}")
