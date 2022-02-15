FROM python:3.9
RUN mkdir /work
WORKDIR /work
COPY . .
RUN apt install grap
RUN pip install .
CMD ["graphviz-py", "-Tsvg", "example/example.py.dot"]