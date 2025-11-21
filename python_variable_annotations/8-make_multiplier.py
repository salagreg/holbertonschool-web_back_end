#!/usr/bin/env python3
""" Module qui contient une fonction qui crée un multiplicateur. """

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Retourne une fonction qui multiplie un nombre
          par un multiplicateur donné."""
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
