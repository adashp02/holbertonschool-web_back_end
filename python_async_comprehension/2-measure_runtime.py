#!/usr/bin/env python3
"""measure_runtime coroutine that will run
async_comprehension 4 times"""
import asyncio
import random
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """this coroutine measures total runtime
    and returns it
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
