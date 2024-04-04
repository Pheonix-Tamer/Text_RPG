# Text RPG
import Title_Screen_text
from Title_Screen_text import print_title_screen
from Rooms import *

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 116


def main():
    os.system(f'mode con: cols={screen_width} lines=30')
    title_screen_options()


# Player Setup #
class Player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.class_type = "fighter"


myplayer = Player()


def title_screen_options():
    while True:
        try:
            print_title_screen()
            option = input("> ").lower()
            if option not in ["play", "help", "quit"]:
                raise ValueError()
        except ValueError:
            print(f"That was not a valid option")
        else:
            break
    if option == "play":
        start_game()
        # print("START")
    elif option == "help":
        help_menu()
        # print("HELP")
    elif option == "quit":
        sys.exit()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#To Pus


def help_menu():
    print()
    print(f"{" HELP ":#^60}")
    print("-> Use the 'North', 'South', 'West', 'East' commands to move!")
    print("-> Use 'Examine' to examine the current room")
    print("-> Use the 'look' command to inspect something in a room")
    print("-> Use 'Quit' to quit the game")
    print("-> Type the commands to perform them")
    input(f"{Title_Screen_text.COLOURS["red"]}-> Press any key to continue{Title_Screen_text.COLOURS["white"]}")
    title_screen_options()


def set_location(curr_loc: Room, direction: str) -> Room:
    if curr_loc.adjacent[direction] is not None:
        return curr_loc.adjacent[direction]
    return curr_loc


def start_game():
    game_logic()
    sys.exit()


def player_start():
    clear_screen()
    p_name = input(f"What is your hero's name?\n> ")
    # p = Player(p_name)
    print(f"Welcome {p_name}")




def game_logic():
    location: Room = entrance
    response = ""
    while response != "quit":
        response = input(f"You see: {location.description}\n> ").lower()
        if response in ["north", "south", "east", "west"]:
            location = set_location(location, response)
            # print(location)
        elif response.startswith("take"):
            pass
        elif response == "look":
            for key in location.adjacent.keys():
                if location.adjacent[key] is not None:
                    print(f"To the {key} you see a(n) {location.adjacent[key]}")
        # if response == "north":
        #     location = location.north
        # elif response == "south":
        #     location = location.south
        # elif response == "east":
        #     location = location.east
        # elif response == "west":
        #     location = location.west


if __name__ == "__main__":
    main()
