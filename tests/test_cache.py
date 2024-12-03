import unittest
from unittest.mock import patch, MagicMock
from app.services.cache import Cache


class TestCache(unittest.TestCase):
    @patch("app.services.cache.redis.StrictRedis")
    def setUp(self, mock_redis):
        """
        Set up a mock Redis instance for testing.
        """
        self.mock_redis = mock_redis.return_value
        self.cache = Cache()

    def test_set_value(self):
        """
        Test that the set method stores the value in Redis.
        """
        key = "product_1"
        value = {"price": 499.99}

        self.cache.set(key, value)

        # Assert that the Redis `set` method was called with the correct parameters
        self.mock_redis.set.assert_called_once_with(key, '{"price": 499.99}')

    def test_get_value(self):
        """
        Test that the get method retrieves the value from Redis.
        """
        key = "product_1"
        value = '{"price": 499.99}'
        self.mock_redis.get.return_value = value

        result = self.cache.get(key)

        # Assert the returned value matches the expected result
        self.assertEqual(result, {"price": 499.99})

    def test_delete_value(self):
        """
        Test that the delete method removes the key from Redis.
        """
        key = "product_1"

        self.cache.delete(key)

        # Assert that the Redis `delete` method was called with the correct key
        self.mock_redis.delete.assert_called_once_with(key)


if __name__ == "__main__":
    unittest.main()
