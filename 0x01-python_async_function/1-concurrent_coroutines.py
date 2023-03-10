#!/usr/bin/env python3
""" 1-module """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ multiple coroutines """
    newList: List[float] = []
    allDelays: List[float] = []
    for i in range(n):
        newList.append(wait_random(max_delay))
    for elems in asyncio.as_completed(newList):
        res = await elems
        allDelays.append(res)
    return allDelays
