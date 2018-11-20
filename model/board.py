class Board:
    pass


def init_board() -> Board:
    board = Board()
    board.first_line = 3
    board.second_line = 4
    board.third_line = 5
    return board


def is_dangerous_state(board: Board) -> bool:
    # As we know that maximum value is 5, we can safely
    # assume there should be no more than 3 positions
    for row in range(3):
        if _calculate_row(board.first_line, board.second_line, board.third_line, row) % 2 == 1:
            return True
    return False


def _calculate_row(first_line, second_line, third_line, row):
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


def _convert_to_binary_string(decimal_number) -> str:
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
