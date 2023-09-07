from os import get_terminal_size, system
import cursor
from sys import stdout


CLEAR_SEQUENCE = "\x1b[1;1H\x1b[2J"


def print_at_(x, y, value):
    # Do not print if the coordinates are outside the terminal
    if x + 1 > width or y + 1 > height or x < 0 or y < 0:
        return

    # sHJldHDSLKFHSD
    # I need to check everytime but I think the terminal is 1-indexed
    print(f"\033[{y + 1};{x * 2 + 1}H{value}", end="")


# Todo: check if system("stty...") works on windows
# Prevent user input from being displayed on the terminal
def hide_stdin():
    system("stty -echo")
    cursor.hide()


# Allow user input to be displayed on the terminal
def show_stdin():
    system("stty echo")
    cursor.show()


def clear_terminal():
    print(CLEAR_SEQUENCE, end="")
    stdout.flush()

size = get_terminal_size()

width = int(size.columns / 2)
height = int(size.lines)
