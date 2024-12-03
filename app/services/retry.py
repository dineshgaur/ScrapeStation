import time
from functools import wraps


def retry(max_retries: int = 3, delay: int = 2, exceptions: tuple = (Exception,)):
    """
    A decorator for retrying a function if it raises an exception.

    Args:
    - max_retries: Maximum number of retries before giving up.
    - delay: Delay (in seconds) between retries.
    - exceptions: Tuple of exception classes to catch.

    Returns:
    - The wrapped function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    print(f"Attempt {attempts} failed with error: {e}")
                    if attempts < max_retries:
                        time.sleep(delay)
                    else:
                        print("Max retries reached. Raising exception.")
                        raise
        return wrapper
    return decorator
