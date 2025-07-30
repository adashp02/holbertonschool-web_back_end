#!/usr/bin/env python3
"""import wait_random from before, create regular func
that takes int max_delay and returns asyncio.Task
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio task for wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random function.

    Returns:
        asyncio.Task: The task created for the wait_random coroutine.
    """
    return asyncio.Task(wait_random(max_delay))
