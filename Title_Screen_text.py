import os

COLOURS = {
    "red": "\033[0;31m",
    "yellow": "\033[1;33m",
    "white": "\033[1;37m"
}

TITLE = """
                           \033[1;33m .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--. 
                           \033[1;33m/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \\
                           \033[1;33m\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
                           \033[1;33m \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
                           \033[1;33m / /\                                                    / /\ 
                           \033[1;33m/ /\ \  \033[0;31m _____ _______   _______  ____________ _____  \033[1;33m  / /\ \\
                           \033[1;33m\ \/ /  \033[0;31m|_   _|  ___\ \ / /_   _| | ___ \ ___ \  __ \ \033[1;33m  \ \/ /
                           \033[1;33m \/ /   \033[0;31m  | | | |__  \ V /  | |   | |_/ / |_/ / |  \/ \033[1;33m   \/ / 
                           \033[1;33m / /\   \033[0;31m  | | |  __| /   \  | |   |    /|  __/| | __  \033[1;33m   / /\ 
                           \033[1;33m/ /\ \  \033[0;31m  | | | |___/ /^\ \ | |   | |\ \| |   | |_\ \ \033[1;33m  / /\ \\
                           \033[1;33m\ \/ /  \033[0;31m  \_/ \____/\/   \/ \_/   \_| \_\_|    \____/ \033[1;33m  \ \/ /
                           \033[1;33m \/ /                                                    \/ / 
                           \033[1;33m / /\.--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
                           \033[1;33m/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \\
                           \033[1;33m\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
                           \033[1;33m `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--' 
"""
MENU = r"""
.-=~=-.                             .-=~=-.                             .-=~=-.                             .-=~=-.
(__  _)-._.-=-._.-=-._.-=-._.-=-._.-(__  _)-._.-=-._.-=-._.-=-._.-=-._.-(__  _)-._.-=-._.-=-._.-=-._.-=-._.-(__  _)
( _ __)                             ( _ __)                             ( _ __)                             ( _ __)
(__  _)    ____  __     ___  _  _   (__  _)   __  __  ____ __    ____   (__  _)     ___   __ __ __ ______   (__  _)
( _ __)    || \\ ||    // \\ \\//   ( _ __)   ||  || ||    ||    || \\  ( _ __)    // \\  || || || | || |   ( _ __)
(__  _)    ||_// ||    ||=||  )/    (__  _)   ||==|| ||==  ||    ||_//  (__  _)   ((   )) || || ||   ||     (__  _)
( _ __)    ||    ||__| || || //     ( _ __)   ||  || ||___ ||__| ||     ( _ __)    \\_/X| \\_// ||   ||     ( _ __)
(__  _)                             (__  _)                             (__  _)                             (__  _)
(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)
`-._.-'                             `-._.-'                             `-._.-'                             `-._.-'
"""


def print_title_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(TITLE)
    print(COLOURS["white"], MENU)
