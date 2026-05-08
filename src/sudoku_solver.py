from typing import Optional


def solve(board: list[list[int]]) -> Optional[list[list[int]]]:
    """Solve the Sudoku puzzle using backtracking. Returns None if unsolvable."""
    board_copy = [row[:] for row in board]
    if _solve_recursive(board_copy):
        return board_copy
    return None


def _solve_recursive(board: list[list[int]]) -> bool:
    """Recursively solve the board using backtracking."""
    row, col = _find_empty(board)
    if row is None:
        return True
    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if _solve_recursive(board):
                return True
            board[row][col] = 0
    return False


def _find_empty(board: list[list[int]]) -> tuple[int, int]:
    """Find the next empty cell (value 0). Returns (row, col) or (None, None) if full."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None


def is_valid_move(board: list[list[int]], row: int, col: int, num: int) -> bool:
    """Check if placing num at board[row][col] is a valid move."""
    if board[row][col] != 0:
        return False
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True
