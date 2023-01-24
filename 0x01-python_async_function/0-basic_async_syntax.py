#!/usr/bin/env python3
""" 0-module """
import random
import asyncio


async def wait_random(max_delay=10):
    """ Write an asynchronous coroutine that takes in an integer argument
    and returns it """
    delay = random.uniform(0, max_delay)
    return delay
