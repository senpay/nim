from model.board import init_board, is_dangerous_state, Board


def test_create_board_should_create_new_board():
    play_board = init_board()
    assert isinstance(play_board, Board)
    assert play_board.first_line == 3
    assert play_board.second_line == 4
    assert play_board.third_line == 5


def test_is_dangerous_state_should_return_true_for_dangerous_state():
    """
    According to logic, if we convert initial state of the boars into binary code, it is going to be:
    3 -> 011
    4 -> 100
    5 -> 101

    0 1 1
    1 0 0
    1 0 1

    2 1 2

    As we have odd sum at the second row - it means board is in dangerous state.
    """
    play_board = init_board()
    assert is_dangerous_state(play_board) is True


def test_is_dangerous_state_should_return_false_for_safe_state():
    """
    According to logic, if we convert initial state of the boars into binary code, it is going to be:
    1 -> 001
    4 -> 100
    5 -> 101

    0 0 1
    1 0 0
    1 0 1

    2 0 2

    As we have even sums at each row - it means board is in safe state.
    """
    play_board = init_board()
    play_board.first_line = 1
    assert is_dangerous_state(play_board) is False
