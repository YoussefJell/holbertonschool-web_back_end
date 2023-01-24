#!/usr/bin/env python3
""" 1-module """
import asyncio
import time
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ multiple coroutines """
    return asyncio.create_task(wait_random(max_delay))
