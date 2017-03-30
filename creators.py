import os
from termcolor import colored

import resources
import tools


# TODO make multithreading


class WordlistBaseMaster:
    def __init__(self):
        self.path = ''
        self.pattern = ''

    def get_path(self):

        while True:
            self.path = input(colored(resources.strings['input_wordlist_master_path'], 'blue'))
            if self.path.rfind('/') < len(self.path) - 1:
                if os.path.exists(self.path):
                    print(colored(resources.strings['warning_file_exists'], 'yellow'))
                    choice = input(resources.strings['prompt_rewrite'])
                    if choice == 'y':
                        print('Ok')
                        return self.path
                    else:
                        print(resources.strings['rewrite_avoiding_message'])
                else:
                    break
            else:
                file_name = input(resources.strings['error_not_a_file'])
                self.path += file_name
                if os.path.exists(self.path):
                    print(colored(resources.strings['warning_file_exists'], 'yellow'))
                    choice = input(resources.strings['prompt_rewrite'])
                    if choice == 'y':
                        print('Ok')
                        return self.path
                    else:
                        print(resources.strings['rewrite_avoiding_message'])
                else:
                    break


class WordlistMaster(WordlistBaseMaster):
    def __init__(self):
        WordlistBaseMaster.__init__(self)
        os.system('clear')
        self.minimum = None
        self.maximum = None
        self.charsets_for_symbols = None

    def get_size(self):
        self.minimum = 0
        self.maximum = 0

        while True:
            input_string = input(colored(resources.strings['input_wordlist_master_len'], 'blue'))
            try:
                lens = input_string.split(',')
                self.minimum = int(lens[0])
                self.maximum = int(lens[1])
                if self.minimum > self.maximum or self.minimum < 1 or self.maximum < 1:
                    raise ValueError
                print(
                    colored(resources.strings['status_wordlist_master_len'].format(self.minimum, self.maximum), 'cyan'))
                break
            except:
                print(colored(resources.strings['input_invalid'], 'red'))
                continue

    @staticmethod
    def get_custom_charset():
        print(tools.colorize_part(resources.strings['status_wordlist_master_custom_charset_title'], 'red', 'must not'))
        while True:
            custom_charset = input('>> ')
            if ' ' in custom_charset:
                print(colored(resources.strings['input_invalid'], 'red'))
                continue
            else:
                return custom_charset

    def prompt_for_charset(self, num):
        charset = ''
        while True:
            print(colored(resources.strings['status_wordlist_master_symbols_specific'].format(num), 'cyan'))
            options = input(colored('>>', 'cyan'))
            keys = options.split(',')
            try:
                one_symbol_charsets = []
                for key in keys:
                    value = resources.charsets[key]
                    if key == 'custom':
                        custom_charset = self.get_custom_charset()
                        one_symbol_charsets.append(custom_charset)
                    else:
                        one_symbol_charsets.append(value)
                    charset = "".join(one_symbol_charsets)

                self.charsets_for_symbols.append(charset)
                break
            except:
                print(colored(resources.strings['input_invalid'], 'red'))
                continue

        del charset

    def get_charsets(self):
        print(colored(resources.strings['status_wordlist_master_symbols'], 'cyan'))
        print(colored(resources.strings['status_wordlist_master_symbols_choose'], 'blue'))
        print(colored(resources.strings['status_wordlist_master_symbols_choose_warning'], 'red'))

        keys = ('az', 'AZ', '09', 'special', 'custom')
        output = ''
        for key in keys:
            output += '[{}]{}\n'.format(colored(key, 'yellow'), resources.charsets.get(key))

        print(output)
        self.charsets_for_symbols = []

        for num in range(self.maximum if self.minimum is not self.maximum else self.minimum):
            self.prompt_for_charset(num)

    def show_summary(self):

        print(colored(resources.strings['title_summary'], 'cyan'))

        print (colored(resources.strings['summary_length'].format(self.minimum, self.maximum), 'green'))
        print (colored(resources.strings['summary_charsets'], 'green'))
        for i in enumerate(self.charsets_for_symbols):
            print(i)
        print (colored(resources.strings['summary_path'].format(self.path), 'green'))
        self.pattern = tools.create_pattern(self.minimum, self.maximum, self.charsets_for_symbols)
        print (colored(resources.strings['summary_pattern'].format(self.pattern), 'green'))

    def start(self):

        print(colored(resources.strings['title_wordlist_master'], 'cyan'))

        self.get_size()
        self.get_charsets()
        os.system('clear')
        self.get_path()
        os.system('mkdir {}'.format(self.path[:self.path.rfind('/')]))
        os.system('clear')
        self.show_summary()
        print(tools.calculate_size(self.minimum, self.maximum, self.charsets_for_symbols) if self.minimum is not self.maximum else tools.calculate_fixed_len_size(self.minimum, self.charsets_for_symbols))

        input(resources.strings['press_any_key'])

        tools.generate_wordlist(self.path, self.pattern, False)


class WordlistByPatternMaster(WordlistBaseMaster):
    def __init__(self):
        WordlistBaseMaster.__init__(self)
        os.system('clear')

    def get_pattern(self):
        while True:
            print(colored(resources.strings['title_wordlist_pattern'], 'cyan'))
            self.pattern = input('>>')
            if tools.validate_pattern(self.pattern):
                return
            else:
                print(resources.strings['error_invalid_pattern'])

    def start(self):
        self.get_pattern()
        self.get_path()

        input(resources.strings['press_any_key'])

        tools.generate_wordlist(self.path, self.pattern, False)
