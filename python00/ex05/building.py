import sys


def building(string: str) -> None:
    upper = sum(1 for c in string if c.isupper())
    lower = sum(1 for c in string if c.islower())
    punctuation = sum(1 for c in string
                      if c in '!"#$%&()*+,-./:;<=>?@\\[]^_`{|}~' or c in "'")
    spaces = sum(1 for c in string if c.isspace())
    digits = sum(1 for c in string if c.isdigit())
    print(f'The text contains {len(string)} characters:',
          f'{upper} upper letters',
          f'{lower} lower letters',
          f'{punctuation} punctuation marks',
          f'{spaces} spaces',
          f'{digits} digits',
          sep='\n')


def read_argv() -> str:
    args = sys.argv
    if len(args) < 2:
        arg = input('What is the text to count?\n') + '\n'
        return arg
    if len(args) > 2:
        raise AssertionError('Wrong number of arguments')
    return args[1]


def main():
    try:
        building(read_argv())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
