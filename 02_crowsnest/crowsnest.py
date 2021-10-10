#!/usr/bin/env python3
"""
Author : Roel Stalman <rstalman@gmail.com>
Date   : 2021-10-07
Purpose: Crow's Nest -- choose the correct article
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article')
    parser.add_argument('word', help='A word')
    parser.add_argument('-s',
                        '--side',
                        help='Side of the ship',
                        metavar='side',
                        type=str,
                        default='larboard')
    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    side = args.side
    word = args.word
    article = "an" if word[0].lower() in 'aeiou' else 'a'
    if word[0].isupper(): article = article.title()
    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


if __name__ == '__main__':
    main()
