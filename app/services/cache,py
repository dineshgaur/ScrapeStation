import redis
import json


class Cache:
    """
    A simple caching mechanism using Redis.
    """

    def __init__(self, host="localhost", port=6379, db=0):
        """
        Initializes the Redis connection.

        Args:
        - host: Redis server host.
        - port: Redis server port.
        - db: Redis database index.
        """
        self.client = redis.StrictRedis(
            host=host, port=port, db=db, decode_responses=True)

    def set(self, key: str, value: any):
        """
        Sets a key-value pair in the cache.

        Args:
        - key: Cache key.
        - value: Cache value.
        """
        self.client.set(key, json.dumps(value))

    def get(self, key: str):
        """
        Retrieves the value for a given key from the cache.

        Args:
        - key: Cache key.

        Returns:
        - The cached value, or None if the key doesn't exist.
        """
        value = self.client.get(key)
        return json.loads(value) if value else None

    def delete(self, key: str):
        """
        Deletes a key-value pair from the cache.

        Args:
        - key: Cache key.
        """
        self.client.delete(key)
