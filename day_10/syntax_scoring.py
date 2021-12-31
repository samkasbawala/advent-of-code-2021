__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def syntax_scoring(input_file_path):
    return get_scoring(get_code_lines(input_file_path))


def get_code_lines(input_file_path):
    with open(input_file_path) as file:
        code_lines = [line.strip() for line in file.readlines()]
    return code_lines


def get_scoring(code_lines):

    corrupt_scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}
    incomplete_scoring = {"(": 1, "[": 2, "{": 3, "<": 4}

    corrupt_scores = []
    incomplete_scores = []
    for line in code_lines:
        stack = []
        incomplete_score = 0
        for bracket in line:
            match bracket:
                case "(":
                    stack.append(bracket)
                case "[":
                    stack.append(bracket)
                case "{":
                    stack.append(bracket)
                case "<":
                    stack.append(bracket)
                case ")":
                    if len(stack) == 0 or stack.pop() != "(":
                        corrupt_scores.append(corrupt_scoring[bracket])
                        break
                case "]":
                    if len(stack) == 0 or stack.pop() != "[":
                        corrupt_scores.append(corrupt_scoring[bracket])
                        break
                case "}":
                    if len(stack) == 0 or stack.pop() != "{":
                        corrupt_scores.append(corrupt_scoring[bracket])
                        break
                case ">":
                    if len(stack) == 0 or stack.pop() != "<":
                        corrupt_scores.append(corrupt_scoring[bracket])
                        break

        # Here if the line is incomplete
        else:
            for bracket in stack[::-1]:
                incomplete_score *= 5
                incomplete_score += incomplete_scoring[bracket]
            incomplete_scores.append(incomplete_score)

    return (
        sum(corrupt_scores),
        sorted(incomplete_scores)[len(incomplete_scores) // 2],
    )


if __name__ == "__main__":
    corrupt_score, incomplete_score = syntax_scoring("input_sample.txt")
    print(
        f"Corrupt score of {corrupt_score} and incomplete score of {incomplete_score}"
    )

    corrupt_score, incomplete_score = syntax_scoring("input.txt")
    print(
        f"Corrupt score of {corrupt_score} and incomplete score of {incomplete_score}"
    )
