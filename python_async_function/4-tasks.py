#!/usr/bin/env python3
"""use wait_n script and alter into new function
that calls another imported function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """calls wait_random n number of times"""

    delays = []
    tasks = []
    """this loop generates list of random numbers using wait_random"""
    for x in range(n):
        tasks.append(task_wait_random(max_delay))

    """using as_completed iterates through tasks"""
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
