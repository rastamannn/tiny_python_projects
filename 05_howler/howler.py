#! /usr/bin/env python3
"""
Author : Anonymous <Anonymous@localhost>
Date   : 2021-10-11
Purpose: Howler (Upper cases input)
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='outfile',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input_str = args.text
    text=''
    if os.path.isfile(input_str):
        in_fh = open(input_str)
        text = in_fh.read()
    else:
        text = input_str
    output_str = text.upper().rstrip()
    
    if args.outfile == '':
        print(output_str)
    else:
        out_fh = open(args.outfile, 'wt')
        out_fh.write(output_str)


# --------------------------------------------------
if __name__ == '__main__':
    main()
