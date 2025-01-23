# ft_package

## Overview
A simple Python package demonstrating list string counting functionality

## Building package
```
flit build
```

## Installation
```
pip install dist/ft_package-0.0.1-py2.py3-none-any.whl
```
or
```
pip install dist/ft_package-0.0.1.tar.gz
```

## Usage
```
from ft_package import count_in_list
```
Example
```
my_list = ['apple', 'banana', 'apple', 'cherry']
result = count_in_list(my_list, 'apple')
print(result) # Output: 2
```

## Features
- Count occurrences of a string in a list
- Simple and lightweight

## Author
jgoldste (jgoldste@student.42bangkok.com)

## License
MIT License
