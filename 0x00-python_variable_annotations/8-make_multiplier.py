#!/usr/bin/env python3
""" 8-make_multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier
    """
    def multiplier_function(n: float) -> float:
        """ multiplier_function """
        return float(n * multiplier)

    return multiplier_function
