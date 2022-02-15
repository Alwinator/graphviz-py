import sys
import argparse
from pathlib import Path

from graphviz_python.graphviz import execute_graphviz
from graphviz_python.parser import convert


parser = argparse.ArgumentParser(description='graphviz-python diagram builder')
parser.add_argument('files', type=Path, nargs='+', help='an integer for the accumulator')

args, unknown = parser.parse_known_args()


def main(_=None):
    """Process command line arguments."""

    file_contents = []

    for file in args.files:
        with open(file) as f:
            file_contents.append(f.read())

    if len(file_contents) == 0:
        file_contents.append(sys.stdin.read())

    for c in file_contents:
        graphviz_content = convert(c)
        execute_graphviz(graphviz_content, unknown)


