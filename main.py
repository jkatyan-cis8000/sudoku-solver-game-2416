#!/usr/bin/env python3
"""Entry point for the Sudoku game."""

import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(abspath(__file__)))

from src.game import Game
from src.ui import UI


def main():
    """Main game loop."""
    print("Welcome to Sudoku!")
    print("\nSelect difficulty:")
    print("  1 - Easy")
    print("  2 - Medium")
    print("  3 - Hard")
    
    try:
        difficulty = int(input("\nEnter difficulty (1-3): ").strip())
        if difficulty not in (1, 2, 3):
            difficulty = 2
    except ValueError:
        difficulty = 2
    
    game = Game(difficulty)
    ui = UI()
    
    game.start_new_game()
    
    while not game.get_status()["game_over"]:
        board_state = game.get_board()
        solution = game.get_solution()
        board_obj = Board(board_state, solution)
        ui.display_board(board_obj)
        
        user_input = ui.get_user_input()
        if user_input is None:
            print("\nThanks for playing!")
            break
        
        row, col, num = user_input
        success, message = game.make_move(row, col, num)
        ui.display_message(message)
        
        if game.check_win():
            ui.display_game_over(True, game.get_status()["attempts"])
            break
    
    if game.get_status()["game_over"] and not game.get_status()["win"]:
        ui.display_game_over(False, game.get_status()["attempts"])


if __name__ == "__main__":
    main()
