#!/usr/bin/env python3
"""Module qui contient une fonction d'aide pour la pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """Retourne un tuple de taille deux contenant"""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
