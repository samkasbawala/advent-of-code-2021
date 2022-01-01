__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


import re


def fold(coords, folds):

    folds = [fold.split()[2] for fold in folds]

    for fold in folds:

        after_fold = set()

        # Fold across y
        if direction := re.search("(?<=^y=)(\\d+)", fold) is not None:
            direction = int(re.search("(?<=^y=)(\\d+)", fold).group(0))

            for x, y in coords:
                if y > direction:
                    after_fold.add((x, (direction - y % direction) % direction))
                else:
                    after_fold.add((x, y))

        # Fold across x
        else:
            direction = int(re.search("(?<=^x=)(\d+)", fold).group(0))
            for x, y in coords:
                if x > direction:
                    after_fold.add(((direction - x % direction) % direction, y))
                else:
                    after_fold.add((x, y))

        coords = after_fold

    return coords


def get_paper_and_folds(input_file_path):
    with open(input_file_path) as file:
        lines = [line.strip() for line in file.readlines()]

    separating_index = lines.index("")
    coords = lines[0:separating_index]
    folds = lines[1 + separating_index : :]

    for i, coord in enumerate(coords):
        x, y = coord.split(",")
        coords[i] = (int(x), int(y))

    return set(coords), folds


def plot(points):
    max_x = max(x for x, _ in points)
    max_y = max(y for _, y in points)

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x, y) in points:
                print("#", end="")
            else:
                print(" ", end="")
        print()

    print()


if __name__ == "__main__":
    coords, folds = get_paper_and_folds("input_sample.txt")
    points = fold(coords, [folds[0]])
    print(len(points))

    coords, folds = get_paper_and_folds("input.txt")
    points = fold(coords, [folds[0]])
    print(len(points))

    coords, folds = get_paper_and_folds("input_sample.txt")
    points = fold(coords, folds)
    plot(points)

    coords, folds = get_paper_and_folds("input.txt")
    points = fold(coords, folds)
    plot(points)
