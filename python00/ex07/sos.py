import sys


def print_morse(string: str):
    """
    Converts a given string to its 'Morse code' representation and prints it

    Args:
    - string (str): the input string to be converted

    Raises:
    - AssertionError: if a character in the string is not alphanumeric or space
    """
    nested_morse = {
                    " ": "/", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
                    "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
                    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
                    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
                    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
                    "X": "-..-", "Y": "-.--", "Z": "--..",
                    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
                    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
                    "8": "---..", "9": "----."
    }
    try:
        morse_str = [nested_morse[c.upper()] for c in string]
        print(*morse_str)
    except KeyError:
        raise AssertionError('AssertionError: the arguments are bad')


def read_argv() -> str:
    """
    Read and validate the command-line arguments

    Returns:
    - str: the argument passed to the script

    Raises:
    - AssertionError: if the number of arguments is not exactly 1
    """
    args = sys.argv
    if len(args) != 2:
        raise AssertionError('AssertionError: the arguments are bad')
    return args[1]


if __name__ == "__main__":
    """
    Main entry point of the script

    - Reads the input text using 'read_argv()' function
    - Processes the text using the 'print_morse()' function
    - Handles and prints any exceptions that occur during execution
    """
    try:
        print_morse(read_argv())
    except Exception as e:
        print(e)
