#!/usr/bin/env python3
"""Module qui contient une fonction asynchrone
          pour générer une liste de nombres aléatoires."""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """Fonction asynchrone qui utilise une compréhension de liste
      pour collecter 10 nombres aléatoires générés par async_generator."""

    random_numbers = [number async for number in async_generator()]
    return random_numbers
