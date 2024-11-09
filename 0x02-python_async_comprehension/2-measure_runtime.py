#!/usr/bin/env python3
"""
Training on making some Async comperhension tasks
"""


import asyncio
import random
import time


async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Function time that function take to process"""
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    elapsed = time.time() - start
    return elapsed
