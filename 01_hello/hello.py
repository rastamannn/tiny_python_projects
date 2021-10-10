#! /usr/bin/env python3
"""
Author:  Python Dude
Purpose: Say hello
"""

import argparse


def get_args():
    """Get the command line arguments"""

    parser = argparse.ArgumentParser(description='Say Hello')
    parser.add_argument('-n',
                        '--name',
                        default='World',
                        metavar='name',
                        help='Name to greet')
    return parser.parse_args()


def main():
    """The main show"""

    args = get_args()
    print('Hello, ' + args.name + '!')


main()
