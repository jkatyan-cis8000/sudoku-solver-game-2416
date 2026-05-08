class Board:
    """Manages the 9x9 Sudoku board state, validation, and move application."""

    def __init__(self, initial_board: list[list[int]], solution: list[list[int]]):
        """Initialize the board with initial state and solution."""
        self._initial = [row[:] for row in initial_board]
        self._current = [row[:] for row in initial_board]
        self._solution = solution

    def place_number(self, row: int, col: int, num: int) -> bool:
        """Place a number at the given position. Returns True if valid, False otherwise."""
        if self._initial[row][col] != 0:
            return False
        if not (1 <= num <= 9):
            return False
        self._current[row][col] = num
        return True

    def remove_number(self, row: int, col: int) -> None:
        """Remove a number from the given cell (set to 0)."""
        if self._initial[row][col] == 0:
            self._current[row][col] = 0

    def get_cell(self, row: int, col: int) -> int | None:
        """Get the value at the given cell. Returns None if out of bounds."""
        if 0 <= row < 9 and 0 <= col < 9:
            return self._current[row][col]
        return None

    def is_complete(self) -> bool:
        """Check if the board is completely filled (no zeros)."""
        for row in range(9):
            for col in range(9):
                if self._current[row][col] == 0:
                    return False
        return True

    def is_correct(self) -> bool:
        """Check if the current board matches the solution."""
        for row in range(9):
            for col in range(9):
                if self._current[row][col] != self._solution[row][col]:
                    return False
        return True

    def display(self) -> str:
        """Return a formatted string representation of the board."""
        lines = []
        for row in range(9):
            row_str = ""
            for col in range(9):
                val = self._current[row][col]
                if val == 0:
                    row_str += ". "
                else:
                    row_str += f"{val} "
                if (col + 1) % 3 == 0 and col < 8:
                    row_str += "| "
            lines.append(row_str.strip())
            if (row + 1) % 3 == 0 and row < 8:
                lines.append("-" * 21)
        return "\n".join(lines)

    def get_initial_value(self, row: int, col: int) -> int:
        """Get the initial (prefilled) value at the given cell."""
        return self._initial[row][col]

    def get_solution(self) -> list[list[int]]:
        """Get the solution board."""
        return self._solution
