#!/usr/bin/env python3
"""working with redis and python."""


from typing import Union
import uuid
import redis


class Cache:
    """Cache class"""
    def __init__(self): 
        """initializes the Cache class."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data in the cache"""
        randomKey = str(uuid.uuid4())
        self._redis.set(randomKey, data)

        return randomKey