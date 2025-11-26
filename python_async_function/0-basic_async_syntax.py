#!/usr/bin/env python3
"""Module qui contient une coroutine qui attend un délai aléatoire"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Coroutine qui attend un délai aléatoire compris entre 0 et max_delay"""
    
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
