#!/usr/bin/env python3
"""type-annotated function that takes a float multiplier
as argument and returns a function that multiplies a float
by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies float by multiplier"""
    def multiply(n: float) -> float:
        """returns a float multiplied by multiplier"""
        return n * multiplier
    return multiply
