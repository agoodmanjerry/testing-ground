#!/bin/python3


def add(a: int, b: int) -> int:
    c = a + b
    return c


c = add(1, 2)
print(c)


def check_quit(*args):
    for arg in args:
        if arg == "q":
            print("Quit!")
            quit()


def get_input():
    input_str = input("Input here:")
    return input_str


while True:
    input_str = get_input()
    check_quit(input_str)
