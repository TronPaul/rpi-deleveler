import argparse
import subprocess
import sys
from pathlib import Path

import os


def delevel(input_files, output_folder, strip_components):
    for if_ in input_files:
        ifp = Path(if_.strip())
        ofp = Path(output_folder, *ifp.parts[strip_components+1:])
        os.makedirs(str(ofp.parent), exist_ok=True)
        rv = subprocess.call(['ffmpeg',
                              '-i', str(ifp),
                              '-c:v', 'libx264', '-level', '4.1',
                              '-c:a', 'copy',
                              '-c:s', 'copy',
                              str(ofp)])
        if rv != 0:
            print('File {} failed'.format(if_), file=sys.stderr)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_folder', default='rpi')
    parser.add_argument('--strip-components', dest='strip_components', type=int, default=0)
    parser.add_argument('input_file', nargs='*')

    args = parser.parse_args()
    if not args.input_file:
        input_files = sys.stdin
    else:
        input_files = args.input_file
    return delevel(input_files, args.output_folder, args.strip_components)


if __name__ == '__main__':
    main()
