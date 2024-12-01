import redis
from typing import Optional


class RedisManager:
    _instance: Optional["RedisManager"] = None
    _redis_client: Optional[redis.Redis] = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._redis_client = redis.Redis(host='localhost', port=6379, db=0, password=None)

    async def initialize(self):
        return self._redis_client