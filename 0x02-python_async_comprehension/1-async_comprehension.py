#!/usr/bin/env python3
"""
Training on making some Async comperhension tasks
"""


import asyncio
import random
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Async comperhension function that return the ready list"""
    lst = [i async for i in async_generator()]
    return lst
