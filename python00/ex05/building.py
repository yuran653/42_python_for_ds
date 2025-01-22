import sys


def building(string: str) -> None:
    """
    Analyzes the given string and prints the count of various character types

    Parameters: string (str): the input string to analyze

    The function counts and prints:
    - The total number of characters in the string
    - The number of uppercase letters
    - The number of lowercase letters
    - The number of punctuation marks
    - The number of spaces
    - The number of digits
    """
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
    """
    Reads the input text to be analyzed from command-line arguments or user input

    Returns: str: the text to analyze

    Behavior:
    - If no command-line arguments are provided, prompts the user for input
    - If more than one argument is provided, raises an AssertionError
    """
    args = sys.argv
    if len(args) < 2:
        arg = input('What is the text to count?\n') + '\n'
        return arg
    if len(args) > 2:
        raise AssertionError('Wrong number of arguments')
    return args[1]


def main():
    """
    Main entry point of the script

    - Reads the input text using 'read_argv()' function
    - Processes the text using the 'building()' function
    - Handles and prints any exceptions that occur during execution
    """
    try:
        building(read_argv())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
