# berke-wordcount-cli

A tiny Python CLI tool that prints line, word, and character counts for a text file.

## Features

- Count lines
- Count words
- Count characters
- Simple command-line usage

## Installation

### From TestPyPI

```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps berke-wordcount-cli
```

### Local development

```bash
pip install -e .
```
## Usage

Run the CLI on a text file:
```bash
wordcount test.txt
```

### Example output

```text
========================
File  : test.txt
Lines : 2
Words : 4
Chars : 23
========================
```