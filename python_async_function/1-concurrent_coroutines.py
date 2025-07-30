#!/usr/bin/env python3
"""import wait_random from previous and write async
that will spawn wait_random n times with specified max_delay
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """calls wait_random n number of times"""

    delays = []
    tasks = []
    """this loop generates list of random numbers using wait_random"""
    for x in range(n):
        tasks.append(wait_random(max_delay))

    """using as_completed iterates through tasks"""
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
