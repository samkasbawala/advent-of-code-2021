__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def dumbo_octopus_part_1(input_file_path, steps=100):
    octopus_grid = get_octopus_grid(input_file_path)

    count = 0
    for step in range(steps):
        count += process_step(octopus_grid)

    return count


def dumbo_octopus_part_2(input_file_path, steps=100):
    octopus_grid = get_octopus_grid(input_file_path)
    total_octopi = sum([len(row) for row in octopus_grid])

    # Loop until flashed count matches number of total octopi
    step = 0
    while True:
        step += 1
        if process_step(octopus_grid) == total_octopi:
            return step


def get_octopus_grid(input_file_path):
    with open(input_file_path) as file:
        octopus_grid = [line.strip() for line in file.readlines()]

    octopus_grid = [list(row) for row in octopus_grid]
    for i, row in enumerate(octopus_grid):
        octopus_grid[i] = list(map(int, row))

    return octopus_grid


def process_step(octopus_grid):

    # Keep track of all the positions that have flashed
    flashed = set()
    while True:
        all_flashed = True
        for x, y in get_needs_to_flash(octopus_grid):
            if (x, y) in flashed:
                continue
            flashed.add((x, y))

            # Flash (increase adjacent octopi)
            increase(octopus_grid, x + 1, y)
            increase(octopus_grid, x - 1, y)
            increase(octopus_grid, x, y + 1)
            increase(octopus_grid, x, y - 1)
            increase(octopus_grid, x + 1, y + 1)
            increase(octopus_grid, x + 1, y - 1)
            increase(octopus_grid, x - 1, y + 1)
            increase(octopus_grid, x - 1, y - 1)

            all_flashed = False

        if all_flashed:
            break

    # Energy level of each octopus increases by 1
    rows = len(octopus_grid)
    for i in range(rows):
        cols = len(octopus_grid[i])
        for j in range(cols):
            octopus_grid[i][j] += 1

    # All positions that have flashed get reset back to 0
    for x, y in flashed:
        octopus_grid[x][y] = 0

    return len(flashed)


def get_needs_to_flash(octopus_grid):

    coords = []
    rows = len(octopus_grid)
    for i in range(rows):
        cols = len(octopus_grid[i])
        for j in range(cols):
            if octopus_grid[i][j] >= 9:
                coords.append((i, j))

    return coords


def increase(octopus_grid, i, j):
    if not (i < 0 or j < 0 or i >= len(octopus_grid) or j >= len(octopus_grid[0])):
        octopus_grid[i][j] += 1


if __name__ == "__main__":
    print(
        f'{dumbo_octopus_part_1("input_sample.txt", 100)} octopi flashed in 100 steps'
    )
    print(f'{dumbo_octopus_part_1("input.txt", 100)} octopi flashed in 100 steps')

    print(
        f'It will take {dumbo_octopus_part_2("input_sample.txt")} steps for all '
        "octopi to flash at once flash"
    )

    print(
        f'It will take {dumbo_octopus_part_2("input.txt")} steps for all octopi to '
        "flash at once flash"
    )
