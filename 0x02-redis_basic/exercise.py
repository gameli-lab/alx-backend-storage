#!/usr/bin/env python3

'''
This is the init module
'''

from functools import wraps
import redis
from uuid import uuid4


def count_calls(method: callable) -> callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}:calls"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: callable) -> callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        input_str = str(args)
        self._redis.rpush(input_key, input_str)
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: any) -> str:
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None):
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        return self.get(key, lambda data: data.decode("UTF-8"))

    def get_int(self, key: str) -> int:
        return self.get(key, lambda data: int.from_bytes(data, "little"))

    def replay(self, method_name: str):
        input_key = f"{method_name}:inputs"
        output_key = f"{method_name}:outputs"
        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        num_calls = len(inputs)
        print(f"{method_name} was called {num_calls} times:")

        for input_str, output_str in zip(inputs, outputs):
            input_args = eval(input_str.decode('utf-8'))
            output = output_str.decode('utf-8')
            print(f"{method_name}(*{input_args}) -> {output}")

