#!/usr/bin/env python3
""" 1-module """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> asyncio.Task:
    """ multiple coroutines """
    newList: List[float] = []
    allDelays: List[float] = []
    for i in range(n):
        newList.append(task_wait_random(max_delay))
    for elems in asyncio.as_completed(newList):
        res = await elems
        allDelays.append(res)
    return allDelays
