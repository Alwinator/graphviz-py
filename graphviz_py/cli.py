import sys
import argparse
from pathlib import Path

from graphviz_py.graphviz import execute_graphviz
from graphviz_py.parser import convert
from graphviz_py.project import Project

parser = argparse.ArgumentParser(description='graphviz-py diagram builder')
parser.add_argument('-v', '--version', action='version', version=f'{Project.name()} version: {Project.version()}')
parser.add_argument('files', type=Path, nargs=argparse.ZERO_OR_MORE, help='an integer for the accumulator')

args, unknown = parser.parse_known_args()


def main(_=None):
    """Process command line arguments."""

    file_contents = []

    if args.files:
        for file in args.files:
            with open(file) as f:
                file_contents.append(f.read())

    if len(file_contents) == 0:
        file_contents.append(sys.stdin.read())

    for c in file_contents:
        graphviz_content = convert(c)
        execute_graphviz(graphviz_content, unknown)


