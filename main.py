import madlibs
import rock_paper_scissors
import hangman
import game
import binarysearch
import minesweeper
import sudoku
game_to_play = input("Type in a letter for one of the programs you want to run: \n \
'g' for guess_number, 'r' for rock_paper_scissors,\n 'h' for hangman, 't' for tic-tac-toe,\n \
'u' for unbeatable tic-tac-toe, 'e' for test unbeatable, 'b' for binary search,\n 'm' for minesweeper, 's' for sudoku solver");

if game_to_play == "g":
    madlibs.pick_a_number_between_one_and_twenty()
elif game_to_play == "r":
    print(rock_paper_scissors.play())
elif game_to_play == "h":
    hangman.play()
elif game_to_play == "t":
    # exec(open('game.py').read())
    game.run_game('normal')
elif game_to_play == "u":
    game.run_game('unbeatable')
elif game_to_play == 'e':
    game.run_unbeatable_tests()
elif game_to_play == 'b':
    binarysearch.run_binary_search()
elif game_to_play == 'm':
    minesweeper.play()
elif game_to_play == 's':
    sudoku.run_sudoku_solver()





