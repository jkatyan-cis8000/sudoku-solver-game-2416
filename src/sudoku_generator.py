import random


def generate_puzzle(difficulty: int) -> list[list[int]]:
    """Generate a valid Sudoku puzzle with the specified difficulty level (1-3)."""
    base_board = _generate_valid_board()
    empty_cells = {
        1: 36,
        2: 46,
        3: 54
    }.get(difficulty, 46)
    puzzle = _remove_cells(base_board, empty_cells)
    return puzzle


def _generate_valid_board() -> list[list[int]]:
    """Generate a complete valid Sudoku board."""
    board = [[0] * 9 for _ in range(9)]
    _fill_board(board)
    return board


def _fill_board(board: list[list[int]]) -> bool:
    """Fill the board using backtracking to create a valid Sudoku solution."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                numbers = list(range(1, 10))
                random.shuffle(numbers)
                for num in numbers:
                    if _is_valid(board, row, col, num):
                        board[row][col] = num
                        if _fill_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def _is_valid(board: list[list[int]], row: int, col: int, num: int) -> bool:
    """Check if placing num at board[row][col] is valid."""
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


def _remove_cells(board: list[list[int]], cells_to_remove: int) -> list[list[int]]:
    """Remove cells from the board to create the puzzle."""
    puzzle = [row[:] for row in board]
    positions = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(positions)
    for row, col in positions[:cells_to_remove]:
        puzzle[row][col] = 0
    return puzzle
