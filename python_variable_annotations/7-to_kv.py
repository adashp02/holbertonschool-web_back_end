#!/usr/bin/env python3
"""type-annotated function that takes string k and int OR float v
and returns as tuple, first element as str, second as square
of int/float annotated as float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple with str and int/float squared as float"""
    return (k, v ** 2)
