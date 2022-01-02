__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


import heapq as hq


def get_risk_level_map_coords(input_file_path, multiplier):
    with open(input_file_path) as file:
        risk_map = [line.strip() for line in file.readlines()]

    height, width = len(risk_map), len(risk_map[0])

    coords = dict()
    for y, row in enumerate(risk_map):
        for x, risk in enumerate(row):
            for y_i in range(multiplier):
                for x_i in range(multiplier):
                    value = int(risk) + x_i + y_i
                    while value > 9:
                        value -= 9
                    coords[(x + x_i * height, y + y_i * width)] = value

    return coords


def find_shortest_path(risk_map_coords):

    # Hold shortest distances/serves as visited collection as well
    distances = dict()

    # Priority queue to hold
    pq = [(0, (0, 0))]
    hq.heapify(pq)

    # End is the bottom right of the square
    end = max(risk_map_coords)

    while pq:
        distance, coord = hq.heappop(pq)
        i, j = coord

        # Node has already been visited if already in dict (greedy alg)
        if coord in distances.keys():
            continue
        else:
            distances[coord] = distance  # We know it is optimal

        # Just return once we reached our destination
        if end == coord:
            return distance

        # Update neighbors in priority queue
        for neighbor in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if neighbor in risk_map_coords:
                hq.heappush(pq, (distance + risk_map_coords[neighbor], neighbor))


if __name__ == "__main__":
    print(find_shortest_path(get_risk_level_map_coords("input_sample.txt", 1)))
    print(find_shortest_path(get_risk_level_map_coords("input.txt", 1)))
    print(find_shortest_path(get_risk_level_map_coords("input_sample.txt", 5)))
    print(find_shortest_path(get_risk_level_map_coords("input.txt", 5)))
