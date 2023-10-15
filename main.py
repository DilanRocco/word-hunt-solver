import sys
from board import Board


# the word hunt destroyer
def run_solver(r, c):
    chars = ["a", "b", "c", "d",
             "e", "f", "g", "h",
             "i", "j", "k", "l",
             "m", "n", "o", "p"]
    num_of_chars = r * c
    while len(chars) < num_of_chars:
        char = input()
        chars.append(char)
    Board(chars, r, c).show_board()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_solver(4, 4)
