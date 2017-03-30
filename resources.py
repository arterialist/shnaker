
strings = {
    'title_main': 'Wordlist generator by arterialist\n',
    'title_wordlist_master': 'Welcome to wordlist generation master.\nI will guide you through pattern creation.\nLet\'s begin!\n\n',
    'title_wordlist_pattern': 'Welcome to generation by pattern. To start,\nplease enter pattern for generation.\nTo learn more about pattern '
                              'structure, see Help.',
    'input_main': 'Please choose action:\n\n1. Generation with master\n2. Generation by pattern\n\n3. Show help\n4. Quit\n\n>> ',
    'input_wordlist_master_len': 'First, enter min and max length of word as comma-separated numbers:\n>> ',
    'input_wordlist_master_path': 'Please specify path to file for wordlist:\n>> ',
    'input_invalid': 'Invalid input',
    'pattern_valid_format_message': 'Pattern is valid - {}',
    'file_exists_format_message': 'File not exists - {}',
    'generating': 'Generating...',
    'invalid_args': 'Input is invalid, check messages above.',
    'invalid_args_count': 'Args count is not 3, not creating wordlist automatically...',
    'python2_error': 'This tool only works with Python 3.x>',
    'press_any_key': 'Press any key to start!!!',
    'rewrite_avoiding_message': 'Avoiding rewriting, reasking...',
    'pattern_broken': 'Pattern is broken!',
    'generation_status': 'Creating words for length {}',
    'status_wordlist_master_len': '\nmin is {} and max is {}, moving on...',
    'status_wordlist_master_custom_charset_title': 'Please enter symbols for custom charset. \nIt must not contain spaces!',
    'status_wordlist_master_symbols': 'Now we are to choose char set for each symbol.\n',
    'status_wordlist_master_symbols_choose': 'Choose any of the charsets listed below.\nYou can choose multiply charsets by separating\ntheir names '
                                             'with commas.',
    'status_wordlist_master_symbols_choose_warning': 'Charsets will be appended as you list them, so please be careful!\n\n',
    'status_wordlist_master_symbols_specific': 'Charsets for symbol {}:\n',
    'warning_file_exists': 'WARNING! File at location you specified already exists! It will be overridden!',
    'prompt_rewrite': 'Do you really want to continue? (y/n)\n>> ',
    'title_summary': 'We are ready to generate your wordlist,\nhere is what we have:\n\n',
    'summary_length': 'Length: min - {}, max - {}\n',
    'summary_charsets': 'Charsets for each symbol:\n',
    'summary_path': 'Path to file with wordlist:\n{}\n',
    'summary_pattern': 'Pattern for this wordlist:\n{}\n',
    'error_not_a_file': 'The path you specified seems to be a directory, please type file name to save:\n>> ',
    'error_invalid_pattern': 'Invalid pattern',
    'unknown_action': 'Unknown action',
    'exiting': 'Now exiting'
}
charsets = {
    'az': 'abcdefghijklmnopqrstuvwxyz',
    'AZ': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '09': '0123456789',
    'special': '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~',
    'custom': 'You can specify custom charset. It can be used as mask.'
}
