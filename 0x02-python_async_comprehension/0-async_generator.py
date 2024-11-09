#!/usr/bin/env python3
"""
Training on making some Async comperhension tasks
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """Making random number in a specific range of 10 numbers"""
    for i in range(10):
        num = random.uniform(1, 10)
        yield num
        await asyncio.sleep(1)
