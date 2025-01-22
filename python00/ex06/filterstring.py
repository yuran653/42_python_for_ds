import sys


def filterstring(string: str, num: int) -> None:
    """
    Filters words from a string that are longer than the specified
    length and prints them

    Parameters:
    - string (str): the input string that contains words to filter
    - num (int): only words longer than lenghts will be included

    Returns:
    - None
    """
    words_list = [word for word in string.split()]
    filterred_words = [word for word in words_list
                       if (lambda x: len(word) > num)(word)]
    print(filterred_words)
    return None


def read_args() -> tuple[str, int]:
    """
    Reads and validates command-line arguments

    Returns:
    - tuple[str, int]: a tuple containing the input string and the length

    Raises:
    - AssertionError: if arguments are missing or invalid
    """
    args = sys.argv
    if len(args) > 3:
        raise AssertionError('AssertionError: the arguments are bad')
    try:
        string = args[1]
        num = int(args[2])
        return string, num
    except Exception:
        raise AssertionError('AssertionError: the arguments are bad')


def main():
    """
    Main entry point of the script

    - Reads the input arguments using the 'read_args()' function
    - Filters the words in the input string using the 'filterstring()' function
    - Handles and prints any exceptions that occur during execution
    """
    try:
        args = read_args()
        filterstring(args[0], args[1])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
