__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def polymerization(input_file_path, steps):
    polymer, rules = get_polymer_and_rules(input_file_path)
    return apply_rules(polymer, rules, steps)


def get_polymer_and_rules(input_file_path):
    with open(input_file_path) as file:
        lines = [line.strip() for line in file.readlines()]

    polymer = list(lines[0])
    rules = lines[2::]
    rules_dict = dict()

    for rule in rules:
        pair, char = rule.split("->")
        rules_dict[pair.strip()] = char.strip()

    return polymer, rules_dict


def apply_rules(polymer, rules, steps):

    # Get count of current characters
    counts = {}
    for char in set(polymer):
        counts[char] = polymer.count(char)

    # Get count of current pairs
    pairs = {}
    for index in range(len(polymer) - 1):
        sub_str = "".join(polymer[index : index + 2])
        pairs[sub_str] = pairs.get(sub_str, 0) + 1

    # Iterate through certain number of steps
    for _ in range(steps):
        new_values = {}

        # Loop through current pairs
        for pair, value in pairs.items():
            if pair in rules.keys():

                # x=value number of two pairs each added
                # x=value number of pairs removed
                char = rules[pair]
                new_values[pair[0] + char] = new_values.get(pair[0] + char, 0) + value
                new_values[char + pair[1]] = new_values.get(char + pair[1], 0) + value
                new_values[pair] = new_values.get(pair, 0) + -value

                # x=value of new characters added
                counts[char] = counts.get(char, 0) + value

        # Update dict with new values
        for pair, value in new_values.items():
            pairs[pair] = pairs.get(pair, 0) + value

    freq = [v for k, v in sorted(counts.items(), key=lambda x: x[1])]
    return freq[-1] - freq[0]


if __name__ == "__main__":
    print(f"Computed value for part 1: {polymerization('input_sample.txt', 10)}")
    print(f"Computed value for part 1: {polymerization('input.txt', 10)}")
    print(f"Computed value for part 2: {polymerization('input_sample.txt', 40)}")
    print(f"Computed value for part 2: {polymerization('input.txt', 40)}")
