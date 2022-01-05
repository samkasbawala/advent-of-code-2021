from __future__ import annotations

__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


from typing import Union, Any
import math
import json


class Node:
    def __init__(self, value, left, right):
        self.parent: Union[Node, None] = None
        self.value: Any = value
        self.left: Union[Node, None] = left
        self.right: Union[Node, None] = right
        self.depth: int = 0

        if self.right:
            self.right.parent = self

        if self.left:
            self.left.parent = self


class Tree:
    def __init__(self, pair: list):
        self.root: Node = self.__construct_tree(pair)
        self.__heightify(self.root, 0)

    def __construct_tree(self, pair: int | Any):
        if isinstance(pair, int):
            return Node(pair, None, None)

        assert len(pair) == 2
        return Node(".", self.__construct_tree(pair[0]), self.__construct_tree(pair[1]))

    def __str__(self) -> str:
        return str(self.get_list())

    def __add__(self, other: Tree) -> Tree:
        return Tree([self.get_list(), other.get_list()])

    def get_list(self):
        def helper(node: Node) -> list:
            if isinstance(node.value, int):
                return node.value
            return [helper(node.left), helper(node.right)]

        return helper(self.root)

    def __heightify(self, node: Node, level: int) -> None:
        if node:
            self.__heightify(node.left, level + 1)
            node.depth = level
            self.__heightify(node.right, level + 1)

    def __find_left_most_node(self, node: Node) -> Node:
        if node.left is None:
            return node
        return self.__find_left_most_node(node.left)

    def __find_right_most_node(self, node: Node) -> Node:
        if node.right is None:
            return node
        return self.__find_right_most_node(node.right)

    def explode(self, node: Node) -> Node:

        # Exploding pairs will always consist of two regular numbers
        node.value = 0
        left_value = node.left.value
        right_value = node.right.value

        # The pair's left value is added to the first regular number to the left of the
        # exploding pair (if any)
        curr_node = node
        while curr_node.parent and curr_node.parent.left is curr_node:
            curr_node = curr_node.parent

        # If curr_node = root, then left most number is the current node that is
        # exploding
        if not (curr_node is self.root):
            left = self.__find_right_most_node(curr_node.parent.left)
            left.value += left_value

        # The pair's right value is added to the first
        # regular number to the right of the exploding pair (if any)
        curr_node = node
        while curr_node.parent and curr_node.parent.right is curr_node:
            curr_node = curr_node.parent

        # If curr_node = root, then right most number is the current node that is
        # exploding
        if not (curr_node is self.root):

            # Find left most value in this sub tree
            right = self.__find_left_most_node(curr_node.parent.right)
            right.value += right_value

        node.left = node.right = None

    def split(self, node: Node) -> None:

        # To split a regular number, replace it with a pair; the left element of the
        # pair should be the regular number divided by two and rounded down, while the
        # right element of the pair should be the regular number divided by two and
        # rounded up
        new_pair_left = math.floor(node.value / 2)
        new_pair_right = math.ceil(node.value / 2)

        left = Node(new_pair_left, None, None)
        node.left = left

        right = Node(new_pair_right, None, None)
        node.right = right

        left.parent = right.parent = node
        left.depth = right.depth = node.depth + 1

        node.value = "."

    def reduce(self):

        # Function that returns node that has to be exploded, visit in order
        def to_explode(node: Node) -> Union[Node, None]:
            ret = None

            def helper(node: Node) -> None:
                if node:
                    helper(node.left)
                    if (
                        node.depth >= 4
                        and isinstance(node.left, Node)
                        and isinstance(node.right, Node)
                        and isinstance(node.left.value, int)
                        and isinstance(node.right.value, int)
                    ):
                        nonlocal ret
                        ret = node if ret is None else ret
                        return
                    helper(node.right)

            helper(node)
            return ret

        # Function that returns node that has to be split, visit in order
        def to_split(node: Node) -> Union[Node, None]:

            ret = None

            def helper(node: Node) -> None:
                if node:
                    helper(node.left)
                    if isinstance(node.value, int) and node.value >= 10:
                        nonlocal ret
                        ret = node if ret is None else ret
                        return
                    helper(node.right)

            helper(node)
            return ret

        while True:
            if node := to_explode(self.root):
                self.explode(node)
                continue
            if node := to_split(self.root):
                self.split(node)
                continue
            break

    def get_magnitude(self) -> int:
        def helper(node: Node) -> int:
            if isinstance(node.value, int):
                return node.value
            return 3 * helper(node.left) + 2 * helper(node.right)

        return helper(self.root)


def get_pairs(input_file_path: str) -> list:
    with open(input_file_path) as file:
        pairs = [pair.strip() for pair in file.readlines()]
    return [json.loads(pair) for pair in pairs]


def snailfish_part_1(input_file_path: str) -> int:
    pairs = get_pairs(input_file_path)

    if len(pairs) == 0:
        return 0
    if len(pairs) == 1:
        tree = Tree(pairs[1])
        tree.reduce()
        return tree.get_magnitude()

    sum = Tree(pairs[0])
    sum.reduce()
    for pair in pairs[1:]:
        sum += Tree(pair)
        sum.reduce()

    return sum.get_magnitude()


def snailfish_part_2(input_file_path: str) -> int:
    pairs = get_pairs(input_file_path)

    if len(pairs) == 0:
        return 0
    if len(pairs) == 1:
        tree = Tree(pairs[1])
        tree.reduce()
        return tree.get_magnitude()

    max_mag = -float("inf")
    for i, pair_1 in enumerate(pairs):
        for j, pair_2 in enumerate(pairs):
            if i == j:
                continue
            sum = Tree(pair_1) + Tree(pair_2)
            sum.reduce()
            max_mag = max(sum.get_magnitude(), max_mag)

    return max_mag


if __name__ == "__main__":

    # Testing list to tree conversion
    assert Tree([[[[[9, 8], 1], 2], 3], 4]).get_list() == [[[[[9, 8], 1], 2], 3], 4]

    assert Tree([7, [6, [5, [4, [3, 2]]]]]).get_list() == [7, [6, [5, [4, [3, 2]]]]]

    assert Tree([[6, [5, [4, [3, 2]]]], 1]).get_list() == [[6, [5, [4, [3, 2]]]], 1]

    assert Tree([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]).get_list() == [
        [3, [2, [1, [7, 3]]]],
        [6, [5, [4, [3, 2]]]],
    ]

    assert Tree([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]).get_list() == [
        [3, [2, [8, 0]]],
        [9, [5, [4, [3, 2]]]],
    ]

    # Testing explosions
    tree = Tree([[[[[9, 8], 1], 2], 3], 4])
    tree.reduce()
    assert tree.get_list() == [[[[0, 9], 2], 3], 4]

    tree = Tree([7, [6, [5, [4, [3, 2]]]]])
    tree.reduce()
    assert tree.get_list() == [7, [6, [5, [7, 0]]]]

    tree = Tree([[6, [5, [4, [3, 2]]]], 1])
    tree.reduce()
    assert tree.get_list() == [[6, [5, [7, 0]]], 3]

    tree = Tree([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]])
    tree.reduce()
    assert tree.get_list() == [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]

    # Testing split and explosion after addition
    tree = Tree([[[[4, 3], 4], 4], [7, [[8, 4], 9]]]) + Tree([1, 1])
    assert tree.get_list() == [[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]
    tree.reduce()
    assert tree.get_list() == [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]

    # Testing magnitude
    assert Tree([[1, 2], [[3, 4], 5]]).get_magnitude() == 143
    assert Tree([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]).get_magnitude() == 1384
    assert Tree([[[[1, 1], [2, 2]], [3, 3]], [4, 4]]).get_magnitude() == 445
    assert Tree([[[[5, 0], [7, 4]], [5, 5]], [6, 6]]).get_magnitude() == 1137
    assert (
        Tree(
            [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
        ).get_magnitude()
        == 3488
    )

    # Part 1
    assert snailfish_part_1("input_sample.txt") == 4140
    print(f'Magnitude of sum = {snailfish_part_1("input.txt")}')

    # Part 2
    assert snailfish_part_2("input_sample.txt") == 3993
    print(f'Max magnitude of two pairs = {snailfish_part_2("input.txt")}')
