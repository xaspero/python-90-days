#!/usr/bin/env python3
# Purpose: Say hello

"""
Author: Wisdom Matthew <w.matthew@outlook.com>
Purpose: Say hello
"""

import argparse

# parser = argparse.ArgumentParser(description='Say hello')
# parser.add_argument('name', help='Name to greet')
# args = parser.parse_args()
# print('Hello, ' + args.name + '!')

# MAKING THE ARGUMENT OPTIONAL

# parser = argparse.ArgumentParser(description='Say hello')
# parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
# args = parser.parse_args()
# print('Hello, ' + args.name + '!')

# ADDING THE main() FUNCTION

# def main():
#     parser = argparse.ArgumentParser(description='Say hello')
#     parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
#     args = parser.parse_args()
#     print('Hello, ' + args.name + '!')

# if __name__ == '__main__':
#     main()

# ADDING THE get_args() FUNCTION

# After I have used pylint (pylint hello.py) to fix the code


# ----------------------------------------------------------------------------------------------
def get_args():
    """ Get the command-line argument """
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        default="World",
                        help="Name to greet")
    return parser.parse_args()


# ----------------------------------------------------------------------------------------------


def main():
    """ It all starts here! """
    args = get_args()
    print("Hello, " + args.name + "!")


# ----------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
