FROM python:3.9
RUN apt-get update && apt-get install graphviz -y
RUN mkdir /work
WORKDIR /work
COPY . .
RUN pip install graphviz_py
CMD ["graphviz-py", "-Tsvg", "example/example.py.dot"]