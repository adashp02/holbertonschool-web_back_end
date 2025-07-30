#!/usr/bin/env python3
"""import wait_n from previous, create a function with ints n and
max_delay as args, measures total execution time and returns
total_time / n as float
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:

    """Measures the total execution time for wait_n(n, max_delay)
    and returns the average time per call. using time.perf_counter
    we can measure start and end time for the wait_n to run.

    Args:
        n (int): The number of calls to wait_n.
        max_delay (int): The maximum delay for each call to wait_random.

    Returns:
        float: Average time taken for each call to wait_n.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    total_time = end_time - start_time
    return total_time / n
