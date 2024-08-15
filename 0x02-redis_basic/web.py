#!/usr/bin/env python3
'''
This is web module
'''
import requests
import redis
from functools import wraps

# Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_result(ttl=10):  # 10 seconds TTL
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            cache_key = f"count:{url}"
            result_key = f"result:{url}"
            count = redis_client.get(cache_key)
            if count is None:
                count = 0
            else:
                count = int(count)
            redis_client.set(cache_key, count + 1)
            result = redis_client.get(result_key)
            if result is None:
                result = func(url)
                redis_client.set(result_key, result, ex=ttl)
            return result
        return wrapper
    return decorator

@cache_result()
def get_page(url: str) -> str:
    response = requests.get(url)
    return response.text
