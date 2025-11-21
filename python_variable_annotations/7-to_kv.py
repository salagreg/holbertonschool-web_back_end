#!/usr/bin/env python3
"""Module qui contient la fonction to_kv et qui retourne un tuple."""

from typing import Tuple


from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Retourne un tuple avec k et le carré de v en float."""
    return (k, float(v ** 2))
