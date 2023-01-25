#!/usr/bin/env python3
"""module docs"""


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """func docs"""
    return [data async for data in async_generator()]
