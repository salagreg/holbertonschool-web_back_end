#!/usr/bin/python3
""" Module qui contient une fonction qui crée un multiplicateur. """


def make_multiplier(multiplier: float) -> callable:
    """Retourne une fonction qui multiplie un nombre
          par un multiplicateur donné."""
    def multiply(number: float) -> float:
        return number * multiplier
    return multiply
