"""
argparse_basics.py
Author: [Your Alias]
Date: April 2025

This script demonstrates basic usage of Python's argparse module.
"""

import argparse

# Create the parser object with a description
parser = argparse.ArgumentParser(description="Argparse demonstration script")

# Define arguments
parser.add_argument('--name', type=str, help='Name of the person')
parser.add_argument('--age', type=int, help='Age of the person')

# Example of action flags (bool switches)
parser.add_argument('--add', action='store_true', help='Simulates adding a profile')
parser.add_argument('--list', action='store_true', help='Simulates listing profiles')

# Parse the arguments from command line
args = parser.parse_args()

# Logic based on parsed arguments
if args.add:
    if args.name and args.age:
        print(f"Adding profile: {args.name}, {args.age} years old.")
    else:
        print("Missing --name or --age for adding profile.")

elif args.list:
    print("Listing all profiles... (example only)")

elif args.name and args.age:
    print(f"Hello, {args.name}. You are {args.age} years old.")

else:
    print("No valid action provided. Use --add or --list or provide name and age.")
