import json
from abc import ABC, abstractmethod


class BaseStorage(ABC):
    """
    Abstract base class for storage mechanisms.
    """
    @abstractmethod
    def save(self, data: list):
        """
        Save data to the storage backend.

        Args:
        - data: List of dictionaries representing the product data.
        """
        pass


class JSONStorage(BaseStorage):
    """
    Concrete implementation of storage using local JSON files.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, data: list):
        """
        Save data to a local JSON file.

        Args:
        - data: List of dictionaries representing the product data.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Data successfully saved to {self.file_path}")
        except Exception as e:
            print(f"Failed to save data: {e}")
