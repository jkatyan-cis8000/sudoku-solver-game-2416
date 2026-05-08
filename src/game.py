class Game:
    """Manages the game state, tracks player progress, and handles win condition."""

    def __init__(self, difficulty: int = 2):
        """Initialize the game with the given difficulty (1-3)."""
        self._difficulty = difficulty
        self._board = None
        self._solution = None
        self._attempts = 0
        self._game_over = False
        self._win = False

    def start_new_game(self) -> None:
        """Initialize a new puzzle and reset game state."""
        from .sudoku_generator import generate_puzzle
        from .sudoku_solver import solve

        puzzle = generate_puzzle(self._difficulty)
        self._solution = solve(puzzle)
        self._board = puzzle
        self._attempts = 0
        self._game_over = False
        self._win = False

    def make_move(self, row: int, col: int, num: int) -> tuple[bool, str]:
        """Make a move at the given position. Returns (success, message)."""
        if self._game_over:
            return False, "Game is already over."

        if not (0 <= row < 9 and 0 <= col < 9):
            return False, "Invalid position."

        if not (1 <= num <= 9):
            return False, "Number must be between 1 and 9."

        if self._board[row][col] != 0:
            return False, "Cell is pre-filled and cannot be changed."

        self._attempts += 1
        if self._solution[row][col] == num:
            self._board[row][col] = num
            return True, "Valid move!"
        else:
            return False, "Incorrect move!"

    def check_win(self) -> bool:
        """Check if the player has won by filling the board correctly."""
        if not self._board:
            return False
        for row in range(9):
            for col in range(9):
                if self._board[row][col] == 0:
                    return False
                if self._board[row][col] != self._solution[row][col]:
                    return False
        self._game_over = True
        self._win = True
        return True

    def get_status(self) -> dict:
        """Return current game status."""
        return {
            "difficulty": self._difficulty,
            "attempts": self._attempts,
            "game_over": self._game_over,
            "win": self._win,
            "board": [row[:] for row in self._board] if self._board else None,
            "solution": [row[:] for row in self._solution] if self._solution else None
        }

    def get_board(self) -> list[list[int]]:
        """Get the current board state."""
        return [row[:] for row in self._board]

    def get_solution(self) -> list[list[int]]:
        """Get the solution board."""
        return [row[:] for row in self._solution]
