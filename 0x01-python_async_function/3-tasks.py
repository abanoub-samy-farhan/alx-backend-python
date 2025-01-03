#!/usr/bin/env python3
"""Tasks"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Wait for a random delay between 0 and max_delay"""
    return asyncio.Task(wait_random(max_delay))
