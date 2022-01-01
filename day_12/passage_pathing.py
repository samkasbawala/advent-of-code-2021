__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


from collections import defaultdict


class Graph:
    """Undirected graph"""

    def __init__(self, input_file_path):
        self.graph = defaultdict(set)
        self.__populate(input_file_path)

    def __populate(self, input_file_path):
        with open(input_file_path) as file:
            edges = [line.strip() for line in file.readlines()]

        for edge in edges:
            node_1, node_2 = edge.split("-")
            self.add_edge(node_1, node_2)

    def add_edge(self, node_1, node_2):
        self.graph[node_1].add(node_2)
        self.graph[node_2].add(node_1)

    def find_paths_part_1(self, start, end):
        paths = set()
        stack = [(start,)]

        while stack:

            path = stack.pop()

            if path[-1] == end:
                paths.add(path)
                continue

            for neighbor in self.graph[path[-1]]:
                if neighbor.isupper() or neighbor not in path:
                    stack.append((*path, neighbor))

        return paths

    def find_paths_part_2(self, start, end):
        paths = set()
        stack = [((start,), False)]

        while stack:

            path, visited_twice = stack.pop()

            if path[-1] == end:
                paths.add(path)
                continue

            for neighbor in self.graph[path[-1]]:
                if neighbor == "start":
                    continue
                elif neighbor.isupper() or neighbor not in path:
                    stack.append(((*path, neighbor), visited_twice))
                elif not visited_twice and path.count(neighbor) == 1:
                    stack.append(((*path, neighbor), True))

        return paths


if __name__ == "__main__":
    print(len(Graph("input_sample.txt").find_paths_part_1("start", "end")))
    print(len(Graph("input.txt").find_paths_part_1("start", "end")))
    print(len(Graph("input_sample.txt").find_paths_part_2("start", "end")))
    print(len(Graph("input.txt").find_paths_part_2("start", "end")))
