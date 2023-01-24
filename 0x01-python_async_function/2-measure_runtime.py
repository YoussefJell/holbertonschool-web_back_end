#!/usr/bin/env python3
""" 1-module """
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
	""" multiple coroutines """
	totalTime: float
	returnedList: List[float] = asyncio.run(wait_n(n, max_delay))
	totalTime = sum(returnedList)
	return totalTime / n
