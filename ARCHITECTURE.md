# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/sudoku_generator.py: Generates valid 9x9 Sudoku puzzles with configurable difficulty
- src/sudoku_solver.py: Solves Sudoku puzzles using backtracking algorithm
- src/board.py: Manages the 9x9 game board state, validation rules, and move application
- src/game.py: Manages game state, tracks player progress, and handles win condition
- src/ui.py: Terminal-based user interface for displaying the board and handling input
- main.py: Entry point that ties all components together

## Interfaces

### sudoku_generator.py
- `generate_puzzle(difficulty: int) -> list[list[int]]`: Creates a puzzle with given difficulty (1-3)
- `remove_cells(board: list[list[int]], cells_to_remove: int) -> list[list[int]]`: Removes cells to create the puzzle

### sudoku_solver.py
- `solve(board: list[list[int]]) -> list[list[int]] | None`: Solves the puzzle, returns None if unsolvable
- `is_valid_move(board: list[list[int]], row: int, col: int, num: int) -> bool`: Checks if a move is valid

### board.py
- `Board` class with methods:
  - `__init__(initial_board: list[list[int]], solution: list[list[int]])`
  - `place_number(row: int, col: int, num: int) -> bool`: Places a number, returns True if valid
  - `remove_number(row: int, col: int)`: Removes a number from a cell
  - `get_cell(row: int, col: int) -> int | None`: Gets the value at a cell
  - `is_complete() -> bool`: Checks if the board is filled
  - `is_correct() -> bool`: Checks if the board matches the solution
  - `display() -> str`: Returns formatted string representation

### game.py
- `Game` class with methods:
  - `__init__(difficulty: int = 2)`
  - `start_new_game()`: Initializes a new puzzle
  - `make_move(row: int, col: int, num: int) -> tuple[bool, str]`: Makes a move, returns (success, message)
  - `check_win() -> bool`: Checks if player has won
  - `get_status() -> dict`: Returns current game status

### ui.py
- `UI` class with methods:
  - `display_board(board: Board)`: Renders the board to terminal
  - `get_user_input() -> tuple[int, int, int] | None`: Gets row, col, number from user
  - `display_message(msg: str)`: Shows messages to user
  - `display_game_over(win: bool, attempts: int)`: Shows end game message

### main.py
- Entry point that initializes Game and UI, runs the game loop

## Shared Data Structures

- `Board State`: 9x9 list of lists of integers (0-9, where 0 = empty)
- `Move`: Tuple of (row: int, col: int, num: int) representing a player move
- `Difficulty Levels`: 1=Easy (36 empty), 2=Medium (46 empty), 3=Hard (54 empty)

## External Dependencies

- None (uses only Python standard library)
