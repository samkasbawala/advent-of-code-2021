__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def seven_segment_display_part_1(input_file_path):

    with open(input_file_path) as file:
        digits = [line.strip() for line in file.readlines()]
    digits = [digit.split("|") for digit in digits]
    digits = [[pattern.strip(), value.strip()] for pattern, value in digits]
    digits = [[pattern.split(), value.split()] for pattern, value in digits]

    count = 0
    for _, values in digits:
        for value in values:
            match len(value):
                case 2:
                    count += 1
                case 3:
                    count += 1
                case 4:
                    count += 1
                case 7:
                    count += 1
                case _:
                    pass

    return count


def seven_segment_display_part_2(input_file_path):

    with open(input_file_path) as file:
        digits = [line.strip() for line in file.readlines()]
    digits = [digit.split("|") for digit in digits]
    digits = [[pattern.strip(), value.strip()] for pattern, value in digits]
    digits = [[pattern.split(), value.split()] for pattern, value in digits]

    sum = 0
    for patterns, values in digits:

        segments = dict()

        # Get segments for unique lengths
        for pattern in patterns:
            match len(pattern):
                case 2:  # is a one
                    segments["1"] = set(pattern)
                case 3:  # is a 7
                    segments["7"] = set(pattern)
                case 4:  # is a four
                    segments["4"] = set(pattern)
                case 7:  # is a 8
                    segments["8"] = set(pattern)
                case _:
                    pass

        left = [
            pattern for pattern in patterns if set(pattern) not in segments.values()
        ]

        for pattern in left:

            # 3 is a superset of 1 (2 and 5 are not)
            if len(pattern) == 5 and len(set(pattern).intersection(segments["1"])) == 2:
                segments["3"] = set(pattern)

            # 5 has three segments in common as 4 (3 has three segments in common as
            # well but 3 will be caught by the if statement above)
            elif (
                len(pattern) == 5 and len(set(pattern).intersection(segments["4"])) == 3
            ):
                segments["5"] = set(pattern)

            # 2 is the only five-segment number left
            elif len(pattern) == 5:
                segments["2"] = set(pattern)

            # 6 is not a superset of 1 (0 and 9 are a superset of 1)
            elif (
                len(pattern) == 6 and len(set(pattern).intersection(segments["1"])) == 1
            ):
                segments["6"] = set(pattern)

            # 9 is a superset of 4 (0 is not)
            elif (
                len(pattern) == 6 and len(set(pattern).intersection(segments["4"])) == 4
            ):
                segments["9"] = set(pattern)

            #  0 is left
            else:
                segments["0"] = set(pattern)

        # Values are unique, use it to look up key (not ideal for speed but whatever)
        output = ""
        for value in values:
            output += [k for k, v in segments.items() if v == set(value)][0]
        sum += int(output)

    return sum


if __name__ == "__main__":
    print(
        f"1, 4, 7, or 8 appears is {seven_segment_display_part_1('input_sample.txt')}"
    )
    print(f"1, 4, 7, or 8 appears is {seven_segment_display_part_1('input.txt')}")
    print(f"Output: {seven_segment_display_part_2('input_sample.txt')}")
    print(f"Output: {seven_segment_display_part_2('input.txt')}")
