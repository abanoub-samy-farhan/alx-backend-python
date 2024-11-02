#!/usr/bin/env python3
"""
Basic async syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function Documented"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> list:
    """Function Documented"""
    delays = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
