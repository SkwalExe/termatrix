from utils import *
from colors import *
from matrix import *
from time import sleep
from help import *
from sys import stdout, argv
import signal

VERSION = "0.1.0"

def version():
    print(f"{BG_PURPLE} Termatrix {RESET}")
    print(f"Version: {PURPLE}{VERSION}{RESET}")


# Update all MatrixColumns objects inside cols
def update_cols(cols):
    for col in cols:
        col.update()

def end(code, reset_cursor = False):
    show_stdin()
    if (reset_cursor):
        print_at_(0, height - 1, "")
    stdout.flush()
    quit(code)

def ctrl_c(*args, **kwargs):
    clear_terminal()
    end(0)

signal.signal(signal.SIGINT, ctrl_c)


def main():
    options = {
        "chars": "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{",
        "color": GREEN,
        "use_colors": True,
        "trailing_color": RED,
        "trailing_length": 1,
        "speed": 96,
        "density": .5,
        # Randomly print characters bold if true
        "bold": False,
        # Print all characters bold if true
        "bold_all": False,
        # Give a random color to each char
        "rainbow": False,
        # If true, makes the rain drops go up instead of down
        "inverse": False,
        # Do one matrix drop per colum to clear the terminal then exit
        "clear_term": False
    }


    # ----- Start parsing args -----
    # Remove program name from arguments
    argv.pop(0)

    # And parse each argument
    while len(argv) > 0:
        arg = argv.pop(0)
        match arg:
            case '--help' | '-h':
                help()
                end(0)

            case '--show-stdin':
                show_stdin()
                end(0)

            case '--version' | '-v':
                version()
                end(0)

            case '--chars' | '-a':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing argument for {PURPLE}{arg}{RESET}")
                    end(1)

                options["chars"] = argv.pop(0)
 
                if not len(options["chars"]) > 0:
                    print(f"{RED}Error: {YELLOW}The argument for {PURPLE}{arg}{YELLOW} must be a non-empty string{RESET}")
                    end(1)

            case '--no-colors' | '-n':
                options["use_colors"] = False

            case '--bold' | '-b':
                options['bold'] = True

            case '--bold-all' | '-ba':
                options['bold_all'] = True

            case '--rainbow' | '-r':
                options['rainbow'] = True
            
            case '--list-colors' | '-lc':
                list_colors()
                end(0)

            case '--inverse' | '-i':
                options['inverse'] = True
            
            case '--clear-term' | '-ct':
                options['clear_term'] = True

            
            case '--color' | '-c':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing argument for {PURPLE}{arg}{RESET}")
                    end(1)
                
                color = argv.pop(0)
                if not color in COLORS:
                    print(f"{RED}Error: {YELLOW}Unknown color : {PURPLE}{color}{RESET}")
                    end(1)
                
                options["color"] = COLORS[color]

            case '--trailing-color' | '-t':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing argument for {PURPLE}{arg}{RESET}")
                    end(1)
                
                color = argv.pop(0)
                if not color in COLORS:
                    print(f"{RED}Error: {YELLOW}Unknown color : {PURPLE}{color}{RESET}")
                    end(1)
                
                options["trailing_color"] = COLORS[color]

            case '--trailing-length' | '-tl':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing argument for {PURPLE}{arg}{RESET}")
                    end(1)
                
                trailing_length = argv.pop(0)
                if not trailing_length.isdigit():
                    print(f"{RED}Error: {YELLOW}The argument for {PURPLE}{arg}{YELLOW} must be an integer{RESET}")
                    end(1)
                
                trailing_length = int(trailing_length)
                if trailing_length < 0:
                    print(f"{RED}Error: {YELLOW}The argument for {PURPLE}{arg}{YELLOW} must be a positive integer or 0{RESET}")
                    end(1)

                options["trailing_length"] = trailing_length

            case '--speed' | '-s':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing argument for {PURPLE}{arg}{RESET}")
                    end(1)
                
                speed = argv.pop(0)
                if not speed.isdigit():
                    print(f"{RED}Error: {YELLOW}The argument for {PURPLE}{arg}{YELLOW} must be an integer{RESET}")
                    end(1)
                
                speed = int(speed)
                if speed < 1 or speed > 100:
                    print(f"{RED}Error: {YELLOW}The argument for {PURPLE}{arg}{YELLOW} must be between 1 and 100{RESET}")
                    end(1)

                options["speed"] = speed

            case '--density' | '-d':
                if len(argv) == 0:
                    print(f"{RED}Error: {YELLOW}Missing argument for {PURPLE}{arg}{RESET}")
                    end(1)

                density = argv.pop(0)
                if not density.isdigit():
                    print(f"{RED}Error: {YELLOW}The argument for {PURPLE}{arg}{YELLOW} must be an integer{RESET}")
                    end(1)
                
                density = int(density)

                if density < 1 or density > 100:
                    print(f"{RED}Error: {YELLOW}The argument for {PURPLE}{arg}{YELLOW} must be between 1 and 100{RESET}")
                    end(1)

                options["density"] = density // 100

            case _:
                print(f"{RED}Error: {YELLOW}Unknown argument : {PURPLE}{arg}{RESET}")
                end(1)

    hide_stdin()

    cols = []

    # Populate the column list with the number of columns that can fit in the terminal width
    for i in range(width):
        cols.append(MatrixCol(options, i))

    delay = (1001 - options["speed"] * 10) / 1000

    # When a matrix drop is created, it is not directly visible because of the whitespace in the bottom of the drop
    first_visible_char = False

    stop = False

    if not options['clear_term']:
        clear_terminal()

    while not stop:
        update_cols(cols)
        # Make the drops fall instantly while the first visible char is not on the screen
        while not first_visible_char:
            update_cols(cols)
            for col in cols:
                if len(col.drops) > 0 and col.drops[0].y + col.drops[0].length > 0:
                    first_visible_char = True
                    break

        if options['clear_term']:
            # Finish is true when for each column one drop fell to the bottom of the screen and disappeared
            finish = True
            for col in cols:
                if not col.at_least_one_drop or not len(col.drops) == 0:
                    finish = False
                    break
            
            if finish:
                stop = True

        stdout.flush()
        sleep(delay)

    end(0, True)

if __name__ == "__main__":
    main()
