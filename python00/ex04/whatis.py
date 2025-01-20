import sys

def main(args):
    if len(args) > 2:
        print('AssertionError: more than one argument is provided')
    else:
        try:
            num = int(args[1])
            if num % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except ValueError:
            print('AssertionError: argument is not an integer')
        except IndexError:
            pass
    print()

args = sys.argv

if __name__ == "__main__":
    main(args)
