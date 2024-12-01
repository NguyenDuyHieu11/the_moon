import redis
from typing import Optional


class RedisClient:
    _instance: Optional["RedisClient"] = None
    _redis_client: Optional[redis.Redis] = None
    room_name_as_key = ""

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._redis_client = redis.Redis(host='localhost', port=6379, db=0, password=None)

    async def initialize(self, room_name):
        self.room_name_as_key = room_name
        return self._redis_client
    