#!/usr/bin/env python3
"""annotate function's parameters and return
values with appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples, each tuple contains
    the element and it's length as int"""
    return [(i, len(i)) for i in lst]
