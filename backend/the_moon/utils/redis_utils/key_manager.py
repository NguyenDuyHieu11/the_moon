from abc import ABC, abstractmethod
from typing import Optional
from redis_client import RedisClient

class KeyManager():
    
    # the connection to redis is an attribute of this class
    redis_client : Optional[RedisClient] = None

    def __init__(self):
        self.redis_client = RedisClient()

    @abstractmethod
    async def generate_key(self, *args):
        pass

    @abstractmethod
    async def set_key(self, key, value):
        pass

    @abstractmethod
    async def get_key(self, key):
        pass