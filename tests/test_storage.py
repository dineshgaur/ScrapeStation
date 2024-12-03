import unittest
import os
import json
from app.services.storage import JSONStorage


class TestJSONStorage(unittest.TestCase):
    def setUp(self):
        """
        Set up a temporary JSON file for testing.
        """
        self.test_file = "test_scraped_data.json"
        self.storage = JSONStorage(self.test_file)

    def tearDown(self):
        """
        Clean up the temporary JSON file after each test.
        """
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_data_success(self):
        """
        Test that data is successfully saved to the JSON file.
        """
        test_data = [
            {
                "product_title": "Test Product",
                "product_price": 999.99,
                "path_to_image": "path/to/image.jpg"
            }
        ]
        self.storage.save(test_data)

        with open(self.test_file, "r") as f:
            saved_data = json.load(f)

        self.assertEqual(saved_data, test_data)

    def test_save_data_empty(self):
        """
        Test saving an empty list to the JSON file.
        """
        test_data = []
        self.storage.save(test_data)

        with open(self.test_file, "r") as f:
            saved_data = json.load(f)

        self.assertEqual(saved_data, test_data)

    def test_save_data_exception(self):
        """
        Test handling an exception when saving data (e.g., invalid file path).
        """
        invalid_storage = JSONStorage("/invalid_path/test.json")

        with self.assertRaises(Exception):
            invalid_storage.save([{"product_title": "Test"}])


if __name__ == "__main__":
    unittest.main()
