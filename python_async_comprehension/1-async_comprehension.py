#!/usr/bin/env python3
"""coroutine that imports previous generator
and it's called async_comprehension"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    this coroutine will collect 10 random numbers 
    using async comprehensing over async_generator
    and return 10 numbers
    """
    return [value async for value in async_generator()]
