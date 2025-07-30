#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that
waits for a random delay between 0 and max_delay (included and
float value) seconds and eventually returns it.
"""
from random import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for random amount of time up to max_delay"""
    delay = random() * max_delay
    """random operates 0 - 1, then we multiply by 10"""
    await asyncio.sleep(delay)
    return delay
