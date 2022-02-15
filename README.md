# WIP: python-graphviz
Allows Python code execution inside of [graphviz](https://graphviz.org/) diagrams

## Install
```bash
pip install python-graphviz
```

## Usage
```bash
python-graphviz -Tsvg example/example.py.dot -o output.svg
python-graphviz -Tpng example/example.py.dot -o output.png
```
```bash
echo 'digraph { A -> B [label="{{= 38 * 73 }}"] }' | python-graphviz -Tsvg > output.svg
```

python-graphviz passes all unknown arguments to graphviz. So you can use all [graphviz arguments](https://graphviz.org/doc/info/command.html).

## Coming soon
- Compartibility with asciidoctor-diagram