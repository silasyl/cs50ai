"""
Tic Tac Toe Player
"""

import math
import copy
from random import random
from random import seed

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for rows in board:
        x_count += rows.count(X)
        o_count += rows.count(O)
    if o_count == x_count:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, rows in enumerate(board):
        for j, col in enumerate(rows):
            if col == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    next_player = player(board)
    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception("wrong action")
    new_board[action[0]][action[1]] = next_player
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == X and board[0][1] == X and board[0][2] == X:
        return X
    if board[1][0] == X and board[1][1] == X and board[1][2] == X:
        return X
    if board[2][0] == X and board[2][1] == X and board[2][2] == X:
        return X
    if board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    if board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    if board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X
    if board[0][0] == O and board[0][1] == O and board[0][2] == O:
        return O
    if board[1][0] == O and board[1][1] == O and board[1][2] == O:
        return O
    if board[2][0] == O and board[2][1] == O and board[2][2] == O:
        return O
    if board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return O
    if board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O
    if board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return O
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winner_player = winner(board)
    empty_count = 0
    if winner_player:
        return True
    for rows in board:
        empty_count += rows.count(EMPTY)
    if empty_count == 0:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    if winner_player == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        target_x = -2
        best_target_x = -2
        current_actions = actions(board)
        for current_action in current_actions:
            current_board = (result(board,current_action))
            target_o = check_o(current_board, best_target_x)
            if target_o > target_x:
                target_x = target_o
                solution = current_action
            if target_o == target_x:
                seed()
                rand = random()
                if rand < 0.5:
                    solution = current_action

    if current_player == O:
        target_o = 2
        best_target_o = 2
        current_actions = actions(board)
        for current_action in current_actions:
            current_board = (result(board,current_action))
            target_x = check_x(current_board, best_target_o)
            if target_x < target_o:
                target_o = target_x
                solution = current_action
            if target_x == target_o:
                seed()
                rand = random()
                if rand < 0.5:
                    solution = current_action

    return solution


def check_x(board, best_target_o):
    """
    Recursive function for X turn
    """
    if terminal(board):
        return utility(board)
    target_x = -2
    best_target_x = -2
    current_actions = actions(board)
    for current_action in current_actions:
        current_board = (result(board, current_action))
        target_o = check_o(current_board, best_target_x)
        if target_o > best_target_o:
            return target_o
        if target_o > target_x:
            target_x = target_o
            best_target_x = target_x
    return target_x


def check_o(board, best_target_x):
    """
    Recursive function for o turn
    """
    if terminal(board):
        return utility(board)
    target_o = 2
    best_target_o = 2
    current_actions = actions(board)
    for current_action in current_actions:
        current_board = (result(board, current_action))
        target_x = check_x(current_board, best_target_o)
        if target_x < best_target_x:
            return target_x
        if target_x < target_o:
            target_o = target_x
    return target_o
