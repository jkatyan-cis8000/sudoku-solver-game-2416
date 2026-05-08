from .board import Board


class UI:
    """Terminal-based user interface for displaying the board and handling input."""

    def __init__(self):
        """Initialize the UI."""
        self._last_message = ""

    def display_board(self, board: Board) -> None:
        """Render the board to terminal."""
        print("\n" + "=" * 23)
        print("       SUDOKU")
        print("=" * 23)
        print()
        board_str = board.display()
        print(board_str)
        print()
        self._print_column_numbers()
        print()

    def _print_column_numbers(self) -> None:
        """Print column numbers below the board."""
        print("  ", end="")
        for col in range(9):
            print(f" {col + 1} ", end="")
            if (col + 1) % 3 == 0 and col < 8:
                print("  ", end="")
        print("\n")

    def get_user_input(self) -> tuple[int, int, int] | None:
        """Get row, col, number from user. Returns None if input is invalid."""
        print("Enter your move (row col number) or 'q' to quit:")
        print("Row, column, and number must be between 1 and 9")
        try:
            user_input = input("> ").strip()
            if user_input.lower() == 'q':
                return None
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid format. Use: row col number")
                return None
            row, col, num = map(int, parts)
            if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
                print("All values must be between 1 and 9")
                return None
            return (row - 1, col - 1, num)
        except ValueError:
            print("Invalid input. Please enter integers.")
            return None

    def display_message(self, msg: str) -> None:
        """Show messages to user."""
        self._last_message = msg
        print(f"  {msg}")

    def display_game_over(self, win: bool, attempts: int) -> None:
        """Show end game message."""
        print("\n" + "=" * 23)
        if win:
            print("   CONGRATULATIONS!")
            print(f"   You solved it in {attempts} attempts!")
        else:
            print("   GAME OVER")
        print("=" * 23)
        print()

    def get_confirmation(self, prompt: str) -> bool:
        """Get yes/no confirmation from user."""
        print(f"\n{prompt} (y/n): ")
        response = input("> ").strip().lower()
        return response in ('y', 'yes')
