#!/usr/bin/env python3
"""Module qui renvoie la somme d'une liste de flottants."""


def sum_list(input_list: float) -> float:
    """Renvoie la somme d'une liste de flottants."""
    total: float = 0.0
    for num in input_list:
        total += num
    return total
