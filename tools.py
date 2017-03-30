from termcolor import colored
import resources


def colorize_part(string, color, part):
    return string.replace(part, colored(part, color))


def colorize_parts(string, color, parts):
    new_string = string
    for part in parts:
        new_string = colorize_part(new_string, color, part)
    return new_string


def format_file_size(size):
    suffixes = 'BKMGTPEZY'
    temp = size >> 10
    index = 0
    while temp:
        temp >>= 10
        index += 1
    return '%g%s' % (round(float(size) / (1 << (10 * index)), 1), suffixes[index])


def delete_all(old_strings, new_string, _str=''):
    for string in old_strings:
        _str = _str.replace(string, new_string)
    return _str


# sample pattern: 4/8.({az|AZ}{09}{az|09}{AZ}{special}{[asdfew23,+=]|az}{special|09}{az|AZ|09})
def create_pattern(minimum, maximum, custom_charsets):
    charset_keys = []
    charsets_keys = []
    user_defined_charsets = {}
    keys = resources.charsets.keys()

    pattern = '{}/{}.('.format(minimum, maximum)
    charsets_string = ''

    index = 0

    for charset in custom_charsets:
        for key in keys:
            if resources.charsets.get(key) in charset:
                charset_keys.append(key)
            else:
                user_charset = delete_all(resources.charsets.values(), '', charset)
                if user_charset is not '':
                    user_defined_charsets[index] = user_charset
        charsets_keys.append(charset_keys)
        charset_keys = []
        index += 1

    del charset_keys
    index = 0

    for _charsets in charsets_keys:
        charsets_string += '|'.join(_charsets)
        if user_defined_charsets.get(index) is not None:
            charsets_string += '[{}]'.format(user_defined_charsets.get(index)) if len(
                charsets_string) is 0 else '|[{}]'.format(user_defined_charsets.get(index))
        pattern = pattern + '{' + charsets_string + '}'
        charsets_string = ''
        index += 1

    pattern += ')'

    return pattern


def validate_pattern(pattern=''):
    if len(pattern) is 0:
        return False

    necessarily_symbols = ['.', '/', '{', '}', '(', ')']

    for symbol in necessarily_symbols:
        if symbol not in pattern:
            return False

    if pattern.index('/') > pattern.index('.') or \
                    pattern.find('(') > pattern.find('{') or \
                    pattern.find('.') > pattern.find('(') or \
                    pattern.rfind(')') != len(pattern) - 1 or \
                    pattern.rfind('}') != len(pattern) - 2:
        return False

    if '|' in pattern and pattern.rfind('|') > pattern.rfind('}') and pattern.find('|') < pattern.find('{'):
        return False

    if '[' in pattern and pattern.rfind(']') > len(pattern) - 3:
        return False

    return True


def parse_pattern(pattern):
    if not validate_pattern(pattern):
        raise Exception(resources.strings['error_invalid_pattern'])

    all_charsets = []

    dot_parts = pattern.split('.', 1)
    minimum, maximum = int(dot_parts[0].split('/')[0]), int(dot_parts[0].split('/')[1])

    dot_parts[1] = dot_parts[1][1:-1]

    splitted_charset_sets = dot_parts[1].split('}{')
    splitted_charset_sets[0] = splitted_charset_sets[0][1:]
    splitted_charset_sets[-1] = splitted_charset_sets[-1][:-1]

    for charset_set in splitted_charset_sets:
        splitted_charsets = charset_set.split('|')
        charset = ''
        for charset_key in splitted_charsets:
            if charset_key[0] is not '[' and charset_key[-1] is not ']':
                try:
                    resources.charsets[charset_key]
                except:
                    raise Exception(resources.strings['error_invalid_pattern'])
                else:
                    charset += resources.charsets.get(charset_key)
            else:
                charset += charset_key[1:-1]
        all_charsets.append(charset)

    return minimum, maximum, all_charsets


def increment_depths(start, depths, charsets):
    if start < 0:
        return

    limit = len(charsets[start])

    if depths[start] + 1 is limit:
        depths[start] = 0
        increment_depths(start - 1, depths, charsets)
    else:
        depths[start] += 1


def get_word(length, depths, charsets):
    word = ['' for unused in range(length)]
    for index in reversed(range(length)):
        word[index] = charsets[index][depths[index]]
    increment_depths(length - 1, depths, charsets)
    return ''.join(word)


def clear_depths(depths):
    for i in range(len(depths)):
        depths[i] = 0


def calculate_fixed_len_size(length, fixed_charsets):
    size = 1
    for i in range(length):
        size *= len(fixed_charsets[i])
    return size


def calculate_size(minimum, maximum, charsets):
    average_size = 0
    for size in range(minimum, maximum + 1):
        print(size)
        average_size += calculate_fixed_len_size(size, charsets)
    return average_size


def generate_words_for_length(length, depths, charsets):
    for index_for_length in range(calculate_fixed_len_size(length, charsets)):
        yield get_word(length, depths, charsets)


def generate_wordlist(file_path, pattern, stdout):
    try:
        minimum, maximum, charsets = parse_pattern(pattern)
    except:
        print(colored(resources.strings['pattern_broken'], 'red'))
        return

    depths = [0 for unused in range(maximum)]

    with open(file_path, 'w') as wordlist_file:
        if minimum is not maximum:
            for length in range(minimum, maximum + 1):
                if not stdout:
                    print(resources.strings['generation_status'].format(length))
                for word in generate_words_for_length(length, depths, charsets):
                    if stdout:
                        print(word)
                    else:
                        wordlist_file.write(word + '\n')

                clear_depths(depths)

        else:
            if not stdout:
                print(resources.strings['generation_status'].format(minimum))
            for word in generate_words_for_length(minimum, depths, charsets):
                if stdout:
                    print(word)
                else:
                    wordlist_file.write(word + '\n')

    clear_depths(depths)

    if not stdout:
        input('Finished!')
