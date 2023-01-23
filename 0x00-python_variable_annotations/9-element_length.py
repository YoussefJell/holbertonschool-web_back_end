#!/usr/bin/env python3
"""9-element_length module"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length """
    return [(j, len(j)) for j in lst]
