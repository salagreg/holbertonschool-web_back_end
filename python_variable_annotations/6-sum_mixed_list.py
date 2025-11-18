#!/usr/bin/python3
"""Module qui retourne la somme d'une liste de nombres entiers et flottants."""


def sum_mixed_list(mxd_lst: list[float | int]) -> float:
    """Retourne la somme d'une liste de nombres entiers et flottants."""
    total: float = 0.0
    for num in mxd_lst:
        total += num
    return total
