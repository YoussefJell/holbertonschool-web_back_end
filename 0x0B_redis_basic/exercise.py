#!/usr/bin/env python3
""" exercise module """
import redis
from typing import Union, Callable, Optional, Any
from uuid import uuid4
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ store history """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapped function """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ decorator """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrap """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """ Cache class """

    def __init__(self):
        """ store method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[int, float, str, bytes]) -> str:
        """ store method """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ get method """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ get_str method """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ get_intt method """
        return self.get(key, int)


def replay(method: Callable):
    """ func """
    key = method.__qualname__
    input = key + ":inputs"
    output = key + ":outputs"
    redis = method.__self__._redis
    count = redis.get(key).decode("utf-8")
    print("{} was called {} times:".format(key, count))
    lstIn = redis.lrange(input, 0, -1)
    lstOut = redis.lrange(output, 0, -1)
    zip = list(zip(lstIn, lstOut))
    for k, v in zip:
        attr, data = k.decode("utf-8"), v.decode("utf-8")
        print("{}(*{}) -> {}".format(key, attr, data))
