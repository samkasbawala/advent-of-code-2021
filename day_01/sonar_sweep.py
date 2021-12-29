__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def sonar_sweep_part_1(input_file_path):
    with open(input_file_path) as file:
        depths = file.readlines()

    greater_than_prev = 0
    for index, depth in enumerate(depths, start=0):
        if index == 0:
            continue
        if int(depth) > int(depths[index - 1]):
            greater_than_prev += 1

    return greater_than_prev


def sonar_sweep_part_2(input_file_path, window):
    with open(input_file_path) as file:
        depths = file.readlines()

    prev = None
    count = 0
    for i in range(0, len(depths) - window + 1):
        if prev is None:
            prev = sum([int(n) for n in depths[i : i + window]])
            continue
        curr = sum([int(n) for n in depths[i : i + window]])
        count = count + 1 if curr > prev else count
        prev = curr

    return count


if __name__ == "__main__":
    print(sonar_sweep_part_1("sonar_sweep_input.txt"))
    print(sonar_sweep_part_2("sonar_sweep_input.txt", 3))
