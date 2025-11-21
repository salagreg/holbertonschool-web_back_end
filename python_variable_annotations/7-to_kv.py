#!/usr/bin/env python3
"""Module qui contient la fonction to_kv et qui retourne un tuple."""

from typing import Tuple


def to_kv(k: str, v: int | float) -> Tuple[str, int | float]:
    """Retourne un tuple contenant deux arguments."""
    return (k, v)
