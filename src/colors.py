# Use the ESC char (ascii 27) to change the colors of the text in the terminal
RED = "\033[91m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
WHITE = "\033[97m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BG_RED = "\033[41m"
BG_YELLOW = "\033[43m"
BG_PURPLE = "\033[45m"
BG_WHITE = "\033[47m"
RESET = "\033[0m"

bar = f"{PURPLE}━━━━━━━━━━━━━━━━━━━━━━{RESET}"


COLORS = {
    "red": RED, 
    "yellow": YELLOW,
    "purple": PURPLE,
    "white": WHITE,
    "green": GREEN,
    "blue": BLUE,
    "cyan": CYAN,
}

def list_colors():
    print()
    print(f"{BG_PURPLE} Available colors {RESET}")
    print(bar)
    for i, color in enumerate(COLORS):
        print(f"{COLORS[color]}{color}{RESET}{'' if i == len(COLORS) - 1 else ' / '}", end="")
    print()