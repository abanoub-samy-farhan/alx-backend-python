#!/usr/bin/env python3

import asyncio
import time

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
start = time.time()
print(asyncio.run(task_wait_n(n, max_delay)))
elapsed = time.time() - start
print(f"Process finished in {elapsed:.2f} seconds")
