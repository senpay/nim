class Board:
    def __init__(self):
        self.lines = [0, 0, 0]


def init_board() -> Board:
    board = Board()
    board.lines[0] = 3
    board.lines[1] = 4
    board.lines[2] = 5
    return board


def update_board(board: Board, line: int, number_of_coins: int) -> Board:
    """
    Subtracts specified number of coins from given line
    """
    board = _clone_board(board)
    board.lines[line] = board.lines[line] - number_of_coins
    return board


def is_dangerous_state(board: Board) -> bool:
    # As we know that maximum value is 5, we can safely
    # assume there should be no more than 3 positions
    print(board.lines[0])
    print(board.lines[1])
    print(board.lines[2])
    for row in range(3):
        print("row=" + str(row))
        print(_calculate_row(board.lines[0], board.lines[1], board.lines[2], row))
        if _calculate_row(board.lines[0], board.lines[1], board.lines[2], row) % 2 == 1:
            return True
    return False


def _calculate_row(first_line: int, second_line: int, third_line: int, row: int):
    return _get_binary_number_at(first_line, row) + _get_binary_number_at(second_line, row)\
           + _get_binary_number_at(third_line, row)


def _get_binary_number_at(decimal_number, position) -> int:
    """
    Converts given decimal_number to binary number and returns what binary number is at given position.

    For instance: 2 -> 010.
    At position 0 it has number 0, at position 1 - 1, at position 2 it has number 0.
    >>> _get_binary_number_at(2, 0)
    0
    >>> _get_binary_number_at(2, 1)
    1
    >>> _get_binary_number_at(2, 2)
    0
    >>> _get_binary_number_at(6, 0)
    1
    >>> _get_binary_number_at(6, 1)
    1
    >>> _get_binary_number_at(6, 2)
    0

    If there's no given position - return zero.
    >>> _get_binary_number_at(2, 2)
    0
    """
    binary_string = _convert_to_binary_string(decimal_number)
    if position == len(binary_string):
        return 0
    return int(binary_string[position])


def _convert_to_binary_string(decimal_number: int) -> str:
    """
    >>> _convert_to_binary_string(1)
    '001'
    >>> _convert_to_binary_string(6)
    '110'
    """
    binary_number = bin(decimal_number)[2:]
    binary_number_length = len(binary_number)
    if binary_number_length < 3:
        binary_number = '0' * (3 - binary_number_length) + binary_number
    return binary_number


def _clone_board(board: Board) -> Board:
    new_board = Board()
    for line in range(len(board.lines)):
        new_board.lines[line] = board.lines[line]
    return new_board
