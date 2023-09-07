from colors import *
from utils import *
import random

options = None



class MatrixDrop:
    def __init__(self, options, x):
        self.options = options
        self.x = x

        # The whitespace length on the bottom of the drop
        self.space_after = random.randint(0, 2 * height * (1 - options['density']))




        # The length of the visible drop must be between 5 and the height of the terminal
        self.length = random.randint(5, height)

        # The total length of the drop including the whitespace and the visible part
        self.total_length = self.length + self.space_after

        # The y position of the top of the drop
        self.y = -self.length - self.space_after

        self.trailing_chars = []

    def print_at(self, x, y, value):
        if self.options['inverse']:
            print_at_(x, height - y, value)
        else:
            print_at_(x, y, value)

    # Makes the drop go down by one unit
    def update(self):
        # Erase the character on the top of the drop (ignoring the whitespace)
        # You can print out of the terminal bounds because the print_at checks for that
        self.print_at(self.x, self.y, " ")

        # The main color
        color = (
            "\033[0m" # Reset color 
            + (
                # Get a random color from the COLORS dict else use the main color
                random.choice(list(COLORS.items()))[1] 
                if self.options['rainbow'] else
                self.options["color"]
            )
        ) if self.options['use_colors'] else ""


        # The trailing characters color
        trailing_color = self.options["trailing_color"] if self.options['use_colors'] else ""

        # Create one trailing character to add to the bottom of the drop
        char = (
            "\033[1m"
            if self.options["bold_all"]
            or (self.options["bold"] and random.choice([True, False]))
            else ""
        ) + random.choice(self.options["chars"]) + " " # Add a whitespace to make the drop erase the possible char next to it because the drops use 1/2 of the columns
        
        # Add one trailing character on the bottom of the drop        
        self.print_at(
            self.x,
            self.y + self.length,
            trailing_color + char,
        )

        self.trailing_chars.append(char)

        # If a drop is no longer part of the trailing characters, change its color to the main color
        if len(self.trailing_chars) > self.options["trailing_length"]:
            self.print_at(
                self.x,
                self.y + self.length - self.options["trailing_length"],
                color + self.trailing_chars.pop(0)
            )

        # Move the drop down by one unit
        self.y += 1


class MatrixCol:
    def __init__(self, options, x):
        self.options = options
        self.x = x
        self.drops = []
        self.at_least_one_drop = False

    def update(self):
        # If there are no drops in the column, create a new one
        if len(self.drops) == 0:
            self.new_drop()

        # Update every drop in the column
        for drop in self.drops:
            # If the drop is out of the screen, remove it
            if drop.y > height:
                self.drops.remove(drop)
                continue

            # Create a new drop if the drop just entered the screen completely
            if drop.y == 0:
                self.new_drop()

            drop.update()

    def new_drop(self):

        # Dont create more than one drop of clear_term is enabled
        if self.at_least_one_drop and self.options['clear_term']:
            return
        
        new_drop = MatrixDrop(self.options, self.x)

        self.at_least_one_drop = True
        self.drops.append(new_drop)
    