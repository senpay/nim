class Board:
    pass


def init_board() -> Board:
    board = Board()
    board.first_line = 3
    board.second_line = 4
    board.third_line = 5
    return board

def is_dangerous_state(board: Board) -> bool:
    return True


def _get_binary_number_at(decimal_number, position) -> int:
    """
    Converts given decimal_number to binary number and returns what binary number is at given position.

    For instance: 2 -> 10.
    At position 0 it has number 0, at position 1 it has number 1.
    >>> _get_binary_number_at(2, 0)
    0
    >>> _get_binary_number_at(2. 1)
    1
    """
