from model.board import *


def test_create_board_should_create_new_board():
    play_board = init_board()
    assert isinstance(play_board, Board)
    assert play_board.lines[0] == 3
    assert play_board.lines[1] == 4
    assert play_board.lines[2] == 5


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
    play_board.lines[0] = 1
    assert is_dangerous_state(play_board) is False


def test_update_boards_does_not_change_original_board():
    play_board = init_board()
    new_board = update_board(play_board, 0, 3)
    assert new_board is not play_board


def test_update_board_does_change_appropriate_line():
    play_board = init_board()
    new_board = update_board(play_board, 1, 3)
    assert new_board.lines[0] == 3
    assert new_board.lines[1] == 1
    assert new_board.lines[2] == 5