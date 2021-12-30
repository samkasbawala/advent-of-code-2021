__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def hydrothermal_venture_part_1(input_file_path):

    with open(input_file_path) as file:
        coords = [line.strip() for line in file.readlines()]

    # Make a list of coordinates
    coords = [coord.split("->") for coord in coords]
    coords = [(p1.strip(), p2.strip()) for p1, p2 in coords]
    for index, coord in enumerate(coords):
        x1, y1 = coord[0].split(",")
        x2, y2 = coord[1].split(",")
        coords[index] = ((int(x1), int(y1)), (int(x2), int(y2)))

    # Store hazard points
    hazards = dict()

    for p1, p2 in coords:
        x1, y1 = p1
        x2, y2 = p2

        # Vertical line
        if x1 == x2:
            for y3 in range(min(y1, y2), max(y1, y2) + 1):
                hazards[f"({x1},{y3})"] = hazards.get(f"({x1},{y3})", 0) + 1

        # Horizontal line
        elif y1 == y2:
            for x3 in range(min(x1, x2), max(x1, x2) + 1):
                hazards[f"({x3},{y1})"] = hazards.get(f"({x3},{y1})", 0) + 1

    return len([k for k, v in hazards.items() if v > 1])


def hydrothermal_venture_part_2(input_file_path):

    with open(input_file_path) as file:
        coords = [line.strip() for line in file.readlines()]

    # Make a list of coordinates
    coords = [coord.split("->") for coord in coords]
    coords = [(p1.strip(), p2.strip()) for p1, p2 in coords]
    for index, coord in enumerate(coords):
        x1, y1 = coord[0].split(",")
        x2, y2 = coord[1].split(",")
        coords[index] = ((int(x1), int(y1)), (int(x2), int(y2)))

    # Store hazard points
    hazards = dict()

    for p1, p2 in coords:
        x1, y1 = p1
        x2, y2 = p2

        # Vertical line
        if x1 == x2:
            for y3 in range(min(y1, y2), max(y1, y2) + 1):
                hazards[f"({x1},{y3})"] = hazards.get(f"({x1},{y3})", 0) + 1

        # Horizontal line
        elif y1 == y2:
            for x3 in range(min(x1, x2), max(x1, x2) + 1):
                hazards[f"({x3},{y1})"] = hazards.get(f"({x3},{y1})", 0) + 1

        # Diagonal line
        else:
            if x1 < x2 and y1 < y2:
                while x1 <= x2 and y1 <= y2:
                    hazards[f"({x1},{y1})"] = hazards.get(f"({x1},{y1})", 0) + 1
                    x1 += 1
                    y1 += 1
            elif x1 > x2 and y1 < y2:
                while x1 >= x2 and y1 <= y2:
                    hazards[f"({x1},{y1})"] = hazards.get(f"({x1},{y1})", 0) + 1
                    x1 -= 1
                    y1 += 1
            elif x1 < x2 and y1 > y2:
                while x1 <= x2 and y1 >= y2:
                    hazards[f"({x1},{y1})"] = hazards.get(f"({x1},{y1})", 0) + 1
                    x1 += 1
                    y1 -= 1
            else:
                while x1 >= x2 and y1 >= y2:
                    hazards[f"({x1},{y1})"] = hazards.get(f"({x1},{y1})", 0) + 1
                    x1 -= 1
                    y1 -= 1

    return len([k for k, v in hazards.items() if v > 1])


if __name__ == "__main__":
    print(f"Overlapping Points: {hydrothermal_venture_part_1('input_sample.txt')}")
    print(f"Overlapping Points: {hydrothermal_venture_part_1('input.txt')}")
    print(f"Overlapping Points: {hydrothermal_venture_part_2('input_sample.txt')}")
    print(f"Overlapping Points: {hydrothermal_venture_part_2('input.txt')}")
