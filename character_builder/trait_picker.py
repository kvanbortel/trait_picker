"""
This program picks random one-sentence traits from a list.
Author: Kayla Van Bortel
"""

import random
from enum import StrEnum

try:
    import colorama
    from colorama import Fore, Style
except ImportError:
    print("Missing colorama module. Using no colors instead. Refer to README.txt for how to install colors.")

    class Fore(StrEnum):
        GREEN = ''
        LIGHTBLACK_EX = ''

    class Style(StrEnum):
        RESET_ALL = ''
else:
    colorama.init()


def pick_traits(num):
    traits = []
    lines = []
    with open("exquisite_character.txt") as file:
        for line in file:
            line = line.strip()
            lines.append(line)
        if num > len(lines):
            print(Fore.LIGHTBLACK_EX + str(num), "is larger than max", len(lines))
            print(Fore.LIGHTBLACK_EX + "Using", len(lines), "instead.")
            print(Style.RESET_ALL, end="")
            num = len(lines)
        while len(traits) < num:
            ri = random.randrange(len(lines))
            traits.append(lines.pop(ri))
    return traits


def main():
    try:
        # Success loop
        while True:
            # Failure loop
            while True:
                try:
                    num = int(input(Fore.GREEN + "Enter number of results: "))
                    break
                except ValueError:
                    print(Fore.LIGHTBLACK_EX + "Input was not an integer. Please try again.")
                    print(Style.RESET_ALL)
                    continue
            print(Style.RESET_ALL, end="")
            if not num:
                break
            traits = pick_traits(int(num))
            for trait in traits:
                print(trait)
            print()
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    main()
