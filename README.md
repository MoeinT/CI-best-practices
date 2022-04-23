## Error types in Python

### mypy
- Mypy is used to do type checking on your Python code. You can add type hints to your code base and mypy will warn you when you use those types incorrectly.

#### see more
- [Type hints cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Getting started](https://mypy.readthedocs.io/en/stable/getting_started.html)
- [Mypy repository](https://github.com/python/mypy)

### flake8
- It is a great toolkit for checking your code base against coding style PEP8, programming errors (like “library imported but unused” and “Undefined name”) and to check cyclomatic complexity.

#### See more 
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

### isort
- 
### Black
- 
### Pylint
- 

## Solutions 

### Black 
Linters such as pycodestyle or flake8 show whether your code is according to PEP8 format, which is the official Python style guide. But the problem is that it gives a burden to the developers to fix this formatting style. Here Black comes into play not only does it report format errors but also fixes them. How to use black to reformat your .py files: 
- Install black using: ```$ pip install black```
- Reformat your code using ```$ black name_of_your_file.py```

Read more about black [here]([![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)) in the documentation. 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### CI/CD actions
- You can check for all the above errors using CI/CD actions. Check out the [this](https://github.com/programmingwithalex/pylinter) repository


