# Really bad code
from math import sqrt


def crazy_function(arg1, another_func):
    def pow_func(arg2):
        return arg2 ** arg2

    value = pow_func(arg1)

    return another_func(value)


argument = 4


def other_func(arg1):
    return sqrt(arg1)


print("Strange value", crazy_function(argument, other_func))
