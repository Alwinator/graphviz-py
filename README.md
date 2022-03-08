# graphviz-py
[![package version](https://img.shields.io/pypi/v/graphviz-py?style=flat-square&color=%2300AA00)](https://pypi.org/project/graphviz-py/)
[![py versions](https://img.shields.io/pypi/pyversions/graphviz-py?style=flat-square)](https://pypi.org/project/graphviz-py/)
[![pypi](https://img.shields.io/github/workflow/status/Alwinator/graphviz-py/Publish%20to%20PyPi?label=Build%20%26%20Publish&style=flat-square)](https://github.com/Alwinator/graphviz-py/actions)
[![license](https://img.shields.io/github/license/Alwinator/graphviz-py?style=flat-square&color=%23006699)](LICENSE)

Allows Python code execution inside of [graphviz](https://graphviz.org/) diagrams

## Example
```dot
graph python_graph {
{{
import math

value = 0.5
sin = math.sin(value)
cos = math.cos(value)
}}

A [label="{{= value }}"];
B [label="{{= sin }}"];
C [label="{{= cos }}"];

A -- B [headlabel="sin"];
A -- C [headlabel="cos"];

}
```

### Output
![output](https://raw.githubusercontent.com/Alwinator/graphviz-py/main/assets/output_file.svg)

## Installation
```bash
pip install graphviz-py
```

**Important: Make sure graphviz is installed!** See [graphviz installation instructions](https://graphviz.org/download/).


## Usage
### Using files
```bash
graphviz-py -Tsvg example/example.py.dot -o output.svg
graphviz-py -Tpng example/example.py.dot -o output.png
```

### Using stdin / pipes
[comment]: <> (echo 'digraph { node [fontname="Arial"]; edge [fontname="Arial"];  A -> B [label="  {{= 38 * 73 }}"] }' | graphviz-py -Tsvg > output.svg)
```bash
echo 'digraph { A -> B [label="{{= 38 * 73 }}"] }' | graphviz-py -Tsvg > output.svg
```
graphviz-py passes all unknown arguments to graphviz. So you can use all [graphviz arguments](https://graphviz.org/doc/info/command.html).

### Output
![output](https://raw.githubusercontent.com/Alwinator/graphviz-py/main/assets/output_pipe.svg)

## Variables
```bash
graphviz-py -Tsvg -a myvalue=5 example/variable_example.py.dot -o output.svg
```
Here we pass a variable called "myvalue" with the value 5

### Output
![output](https://raw.githubusercontent.com/Alwinator/graphviz-py/main/assets/output_variable.svg)

## Security
Please keep in mind that graphviz-py executes all Python code in the diagram. So make sure that your diagrams dies not include harmful code.

## Coming soon
- Compartibility with asciidoctor-diagram ([Status: Implemented & Approved, waiting for merging](https://github.com/asciidoctor/asciidoctor-diagram/pull/379))

## Arguments
```bash
# graphviz-py --help
usage: graphviz-py [-h] [-v] [-d] [-a ARGUMENT] [files [files ...]]

graphviz-py diagram builder

positional arguments:
  files                 the paths to the graphviz-py files

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d, --debug           show debug information
  -a ARGUMENT, --argument ARGUMENT
```
