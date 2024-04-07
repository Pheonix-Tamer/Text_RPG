# Text RPG
import Title_Screen_text
from Characters import Player
from Title_Screen_text import print_title_screen
from Rooms import *

import inflect
import sys
import os

screen_width = 116

k = inflect.engine()


def main():
    os.system(f"mode con: cols={screen_width} lines=30")
    title_screen_options()


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
    os.system("cls" if os.name == "nt" else "clear")


def help_menu():
    print()
    # print(f"{" HELP ":#^60}")
    print("-> Use the 'North', 'South', 'West', 'East' commands to move!")
    print("-> Use 'Examine' to examine the current room")
    print("-> Use the 'Look' command to inspect something in a room")
    print("-> Use 'Quit' to quit the game")
    print("-> Type the commands to perform them")
    # input(f"{Title_Screen_text.COLOURS["red"]}-> Press any key to continue{Title_Screen_text.COLOURS["white"]}")
    title_screen_options()


def set_location(curr_loc: Room, direction: str) -> Room:
    if curr_loc.adjacent[direction] is not None:
        return curr_loc.adjacent[direction]
    print("You cannot go that way")
    return curr_loc


def start_game():
    player = player_start()
    game_logic(player)
    sys.exit()


def player_start() -> Player:
    clear_screen()
    p_name = input(f"What is your hero's name?\n> ")
    p = Player(p_name)
    print(f"Welcome {p.name} to the adventure!!\nYou are a {p.class_type}")
    p.hp = 20
    p.mp = 0
    return p


def game_logic(player):
    location: Room = entrance
    response = ""
    while response != "quit" or response != "q":
        # Quit the game
        response = input(f"You see: {location.description}\n> ").lower()
        if response in ["north", "south", "east", "west"]:
            # Move location
            location = set_location(location, response)
        elif response.startswith("take"):
            if type(location) is not ItemRoom:
                print("There is no item to take")
                continue
            line = response.split(maxsplit=1)
            to_take = line[1]
            if to_take not in location.items:
                print("There is no item here with that name")
                continue
            player.add_item(to_take)
            location.remove_item(to_take)
            pass
        elif response in ["look", "l"]:
            # Look around
            look_around(location)
        elif response == "attack":
            # Attack an enemy
            if type(location) is CombatRoom:
                print("combat here")
            else:
                print("There is nothing to attack")
        elif response.startswith("ex"):
            # Examine an item
            if type(location) is ItemRoom:
                print("there is an item here")
            else:
                print("There is nothing to examine")
        else:
            # Default
            print("I don't know that command")


def look_around(location):
    for key in location.adjacent.keys():
        if location.adjacent[key] is not None:
            # print(f"To the {key} you see a(n) {location.adjacent[key].name.lower()}")
            print(
                f"To the {key} you see",
                k.an(location.adjacent[key].name.lower()),
            )


if __name__ == "__main__":
    main()
