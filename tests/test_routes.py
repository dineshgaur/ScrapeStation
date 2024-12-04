import unittest
from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.main import app
from unittest.mock import patch

client = TestClient(app)


class TestRoutes(unittest.TestCase):
    @patch("app.services.scraper.Scraper.scrape_all")
    @patch("app.services.storage.JSONStorage.save")
    @patch("app.services.notifier.ConsoleNotifier.notify")
    def test_scrape_endpoint_success(self, mock_notify, mock_save, mock_scrape_all):
        mock_scrape_all.return_value = [
            {"product_title": "Test Product", "product_price": 499.99, "path_to_image": "path/to/image.jpg"}
        ]

        response = client.post(
            "/api/scrape/",
            json={"limit": 5, "proxy": None},
            headers={"Authorization": "your_static_token"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")

    def test_scrape_endpoint_unauthorized(self):
        response = client.post(
            "/api/scrape/",
            json={"limit": 5, "proxy": None},
            headers={"Authorization": "wrong_token"}
        )
        self.assertEqual(response.status_code, 403)

    def test_scrape_endpoint_bad_request(self):
        """
        Test the /api/scrape/ endpoint with invalid input data.
        """
        response = client.post(
            "/api/scrape/",
            json={"limit": -1, "proxy": None},
            headers={"Authorization": "your_static_token"}
        )
        # Unprocessable Entity (validation error)
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
