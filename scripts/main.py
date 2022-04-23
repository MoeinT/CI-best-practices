import math
import os


def func1(a, b) -> int:
    return math.floor(a + b)


def func2(a, b, c) -> str:
    return os.getcwd()


def foo(a: str) -> str:
    return "(" + a.strip() + ")"


def get_length(text: str) -> str:

    i = 0
    for letter in text:
        i += 1

    return f"The word has the length {i}"


print(func1(2.2, 3.1))
print(foo("Hello, world"))
print(get_length("Hello, world"))
