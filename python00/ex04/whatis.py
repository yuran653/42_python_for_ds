import sys


def whatis(args):
    if len(args) > 2:
        raise AssertionError('AssertionError: '
                             'more than one argument is provided')
    else:
        try:
            num = int(args[1])
            if num % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            raise AssertionError('AssertionError: '
                                 'argument is not an integer')
        except IndexError:
            pass
    print()


def main():
    args = sys.argv
    try:
        whatis(args)
    except Exception as e:
        print(e)
        print()


if __name__ == "__main__":
    main()
