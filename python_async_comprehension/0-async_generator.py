#!/usr/bin/env python3
"""Module qui contient une fonction asynchrone
        générant des nombres aléatoires."""

import asyncio
import random


async def async_generator():
    """Fonction asynchrone qui génère un nombre aléatoire
        entre 0 et 10 toutes les secondes, pendant 10 secondes."""

    for i in range(10):
        await asyncio.sleep(1)
        tasks = random.uniform(0, 10)
        yield tasks
