__author__ = "Sam Kasbawala"
__credits__ = ["Sam Kasbawala"]

__maintainer__ = "Sam Kasbawala"
__email__ = "samfrnds093@gmail.com"
__status__ = "Development"


def giant_squid_part_1(input_file_path):

    # Get the numbers and the boards
    numbers, boards = get_numbers_boards(input_file_path)

    # Loop through the numbers and each board
    for number in numbers:
        for board in boards:
            for row in board:
                for index, num in enumerate(row):
                    row[index] = "-1" if num == number else num

            # After the number for a board has been evaluated, check for bingo
            if check_board(board):
                sum = 0
                for row in board:
                    for num in row:
                        sum += int(num) if num != "-1" else 0
                return sum * int(number)


def giant_squid_part_2(input_file_path):

    # Get the numbers and the boards
    numbers, boards = get_numbers_boards(input_file_path)

    # Loop through the numbers and each board
    index = 0
    while len(boards) > 1:
        for board in boards:
            for row in board:
                for i, num in enumerate(row):
                    row[i] = "-1" if numbers[index] == num else num

        # Create a new list of boards that have not won yet
        boards = [board for board in boards if check_board(board) is False]
        index += 1

    # Play until the last board wins
    while True:
        for board in boards:
            for row in board:
                for i, num in enumerate(row):
                    row[i] = "-1" if numbers[index] == num else num

            if check_board(board):
                sum = 0
                for row in board:
                    for num in row:
                        sum += int(num) if num != "-1" else 0
                return sum * int(numbers[index])
        index += 1


# Read the numbers and boards from the file
def get_numbers_boards(input_file_path):
    with open(input_file_path) as file:
        input = [line.strip() for line in file.readlines()]

    numbers = input[0].split(",")

    boards = []
    index = 2
    while index < len(input):
        board = []
        while input[index] != "":
            row = input[index].strip().split()
            board.append(row)
            index += 1
            if index >= len(input):
                break
        index += 1
        boards.append(board)

    return numbers, boards


# Check board for bingo
def check_board(board):

    # Check rows
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += int(board[i][j])
        if sum == -5:
            return True

    # Check columns
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += int(board[j][i])
        if sum == -5:
            return True

    # False
    return False


if __name__ == "__main__":
    print(f"Final score of 1st board to win: {giant_squid_part_1('input_sample.txt')}")
    print(f"Final score of 1st board to win: {giant_squid_part_1('input.txt')}")
    print(f"Final score of last board to win: {giant_squid_part_2('input_sample.txt')}")
    print(f"Final score of last board to win: {giant_squid_part_2('input.txt')}")
