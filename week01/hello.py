#!/usr/bin/env python3
"""
GREETING PROGRAM - Command-line Hello Tool with Required Name

This program greets the user by their name using a required command-line argument.

WHAT IT DOES:
  - Takes a required name argument from the command line
  - Prints a personalized greeting: "Hello, [name]!"
  - Displays error if name is not provided

HOW TO USE IT:
  ./hello.py Alice      # Output: Hello, Alice!
  ./hello.py Bob        # Output: Hello, Bob!

TECHNICAL DETAILS:
  - Uses argparse module to handle command-line arguments
  - Argument "name" is a positional argument (required)
  - Provides helpful --help output for users
  - Uses Python f-strings for string formatting
"""

import argparse

# Create a parser to handle command-line arguments
parser = argparse.ArgumentParser(description="Say hello")

# Define a required positional argument for the user's name
parser.add_argument("name", help="Your name")

# Parse the command-line arguments
args = parser.parse_args()

# Print the greeting
print(f"Hello, {args.name}!")

