#!/usr/bin/python3

import os
import sys
from termcolor import colored
import tools
import creators
from resources import strings

option = 0
last_message = ''


def master_generation():
    creators.WordlistMaster().start()


def pattern_generation():
    creators.WordlistByPatternMaster().start()


def show_help():
    os.system('clear')
    with open('help.txt', 'r') as help_file:
        for line in help_file.readlines():
            print(colored(line[:-1], 'green'))
    input()


def unknown():
    global last_message
    last_message = strings['unknown_action']


cases = {
    1: master_generation,
    2: pattern_generation,
    3: show_help,
}


def resolve_input(i):
    if i == 4:
        print(strings['exiting'])
    else:
        action = cases.get(i, unknown)
        action()


try:
    import thread
except:
    if len(sys.argv) is 3:
        pattern = sys.argv[1]
        path_or_flag = sys.argv[2]

        silent = path_or_flag in ('-s', '--silent')

        pattern_valid = tools.validate_pattern(pattern)
        file_not_exists = True
        if not silent:
            file_not_exists = not os.path.exists(path_or_flag)

        if pattern_valid and file_not_exists:
            tools.generate_wordlist(path_or_flag, pattern, silent)
        else:
            print(strings['pattern_valid_format_message'].format(pattern_valid))
            print(strings['file_exists_format_message'].format(file_not_exists))
            print(strings['invalid_args'])
            exit()
    else:
        last_message = strings['invalid_args_count']
        while option != 4:
            os.system('clear')
            print(colored(strings['title_main'], 'green'))
            print(colored(last_message + '\n', 'red'))

            input_action = strings['input_main']
            input_action = tools.colorize_parts(input_action, 'yellow', ('1.', '2.', '3.', '4.'))
            try:
                user_input = input(input_action)
                option = int(user_input)
            except:
                last_message = strings['input_invalid']
                continue

            resolve_input(option)
else:
    print(colored(strings['python2_error'], 'red'))
    exit()
