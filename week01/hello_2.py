#!/usr/bin/env python3
"""
GREETING PROGRAM - Command-line Hello Tool

This program greets the user by name using command-line arguments.

WHAT IT DOES:
  - Takes an optional name argument from the command line
  - If no name is provided, it defaults to "World"
  - Prints a personalized greeting: "Hello, [name]!"

HOW TO USE IT:
  ./hello_2.py              # Output: Hello, World!
  ./hello_2.py -n Alice     # Output: Hello, Alice!
  ./hello_2.py --name Bob   # Output: Hello, Bob!

TECHNICAL DETAILS:
  - Uses argparse module to handle command-line arguments
  - Argument '-n' or '--name' accepts a name value
  - The argument is optional (default='World')
  - Uses Python f-strings for string formatting
"""

import argparse

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument('-n', '--name', metavar='name', default='World', help="Your name")
args = parser.parse_args()
print(f"Hello, {args.name}!")

