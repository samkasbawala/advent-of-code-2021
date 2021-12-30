__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def lanternfish(input_file_path, days):

    with open(input_file_path) as file:
        ages = [line.strip() for line in file.readlines()]
    ages = [age for age in ages[0].split(",")]

    # Count how many fish at each age
    ages_dict = dict()
    for age in ages:
        ages_dict[age] = ages_dict.get(age, 0) + 1

    # Move counts around in the dictionary
    for _ in range(days):
        new_ages = {}
        for age in range(9):
            if str(age) in ages_dict.keys():

                # All 0s give birth to 8s and all 0s turn into 6s
                if str(age) == "0":
                    new_ages["8"] = ages_dict.get("0", 0) + new_ages.get(str("8"), 0)
                    new_ages["6"] = ages_dict.get("0", 0) + new_ages.get(str("6"), 0)

                # Decrement
                else:
                    new_ages[str(age - 1)] = ages_dict.get(str(age), 0) + new_ages.get(
                        str(age - 1), 0
                    )

        ages_dict = new_ages

    return sum(ages_dict.values())


if __name__ == "__main__":
    print(f"Number of fish after 18 days: {lanternfish('input_sample.txt', 18)}")
    print(f"Number of fish after 80 days: {lanternfish('input_sample.txt', 80)}")
    print(f"Number of fish after 256 days: {lanternfish('input_sample.txt', 256)}")
    print(f"Number of fish after 80 days: {lanternfish('input.txt', 80)}")
    print(f"Number of fish after 256 days: {lanternfish('input.txt', 256)}")
