from os import name, system


def clear_terminal():
    if name == 'posix':
        system('clear')
    else:
        system('cls')
