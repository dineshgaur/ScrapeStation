import unittest
from fastapi.testclient import TestClient
from app.main import app
from unittest.mock import patch

client = TestClient(app)


class TestRoutes(unittest.TestCase):
    @patch("app.services.scraper.Scraper.scrape_all")
    @patch("app.services.storage.JSONStorage.save")
    @patch("app.services.notifier.ConsoleNotifier.notify")
    def test_scrape_endpoint_success(self, mock_notify, mock_save, mock_scrape_all):
        """
        Test the /api/scrape/ endpoint for successful scraping.
        """
        mock_scrape_all.return_value = [
            {"product_title": "Test Product", "product_price": 499.99,
                "path_to_image": "path/to/image.jpg"}
        ]

        response = client.post(
            "/api/scrape/",
            json={"limit": 1, "proxy": None},
            headers={"Authorization": "your_static_token"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "success")
        self.assertEqual(response.json()["products_scraped"], 1)
        mock_scrape_all.assert_called_once()
        mock_save.assert_called_once()
        mock_notify.assert_called_once()

    def test_scrape_endpoint_unauthorized(self):
        """
        Test the /api/scrape/ endpoint for unauthorized access.
        """
        response = client.post(
            "/api/scrape/",
            json={"limit": 1, "proxy": None},
            headers={"Authorization": "wrong_token"}
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()["detail"], "Unauthorized")

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
