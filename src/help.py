from colors import *

def help():
    print() 
    print(f"{BG_PURPLE} Termatrix {RESET}")
    print(bar)
    print(f"Author: {PURPLE}SkwalExe <Leopold Koprivnik>{RESET}")
    print(f"Github: {PURPLE}https://github.com/SkwalExe{RESET}")
    print(bar)
    print(f"Cool and customizable Matrix effect in your terminal")
    print(bar)
    print(f"Options:")
    print(f"\t{PURPLE}--show-stdin : {YELLOW}If your cursor is not visible after playback, use this option to show it again")
    print(f"\t{PURPLE}-h, --help : {YELLOW}Show this help message and exit")
    print(f"\t{PURPLE}-v, --version : {YELLOW}Show the version number and exit")
    print(bar)
    print(f"\t{PURPLE}-a, --chars [text]: {YELLOW}A string of characters to use in the matrix")
    print(f"\t{PURPLE}-n, --no-colors: {YELLOW}Don't use colors")
    print(f"\t{PURPLE}-lc, --list-colors: {YELLOW}List every available color")
    print(f"\t{PURPLE}-c, --color [color name]: {YELLOW}The color to use for the matrix")
    print(f"\t{PURPLE}-t, --trailing-color [color name]: {YELLOW}The color to use for the trailing characters")
    print(f"\t{PURPLE}-tl, --trailing-length [int]: {YELLOW}The length of the trailing characters")
    print(f"\t{PURPLE}-s, --speed [int 1-100]: {YELLOW}The speed of the matrix effect")
    print(f"\t{PURPLE}-d, --density [int 1-100]: {YELLOW}The density of the matrix effect")
    print(f"\t{PURPLE}-b, --bold: {YELLOW}Randomly print characters bold")
    print(f"\t{PURPLE}-ba, --bold-all: {YELLOW}Print all characters bold")
    print(f"\t{PURPLE}-r, --rainbow: {YELLOW}Give a random color to each char")
    print(f"\t{PURPLE}-i, --inverse: {YELLOW}Makes the rain drops go up instead of down")
    print(f"\t{PURPLE}-ct, --clear-term: {YELLOW}Do one matrix drop per colum to clear the terminal then exit (cannot be used with -st)")
    
    
    print(bar)

    print()