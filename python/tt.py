#!/bin/python

# from rr.RR import tclass as tc
from rr import tclass as tc

print("hello!")
tc("t").rr()
tc("ewt").rr()
tc("5")


# for i in range(3):
#     print(2 + i)
#
#
# def plus(a, b):
#     c = a + b
#     return c


def echo(g: str) -> None:
    return print(g)


echo("hihi")
