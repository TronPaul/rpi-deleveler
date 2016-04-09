import argparse
import subprocess
import os
import re
from xml.etree.ElementTree import parse

OVER_LEVEL_PATTERN = re.compile('@L(?:4\.[2-9]|5(?:\.[0-9]+)?)')


def get_mkv_info(mkv_path):
    r, w = os.pipe()
    subprocess.Popen(['mediainfo', '--output=XML', mkv_path], stdout=os.fdopen(w))
    return parse(os.fdopen(r))


def over_leveled(mkv_info):
    format_profile = mkv_info.find("./File/track[@type='Video']/Format_profile").text
    return OVER_LEVEL_PATTERN.search(format_profile) is not None


def level_check(input_files):
    for if_ in input_files:
        if over_leveled(get_mkv_info(if_)):
            print(if_)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', nargs='+')

    args = parser.parse_args()
    return level_check(args.input_file)

if __name__ == '__main__':
    main()
