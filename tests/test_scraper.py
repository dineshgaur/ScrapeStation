import unittest
from unittest.mock import patch
from app.services.scraper import Scraper


class TestScraper(unittest.TestCase):
    @patch("app.services.scraper.requests.get")
    def test_scrape_page_success(self, mock_get):
        """
        Test that scrape_page successfully parses product data.
        """
        # Mock HTML content of the response
        mock_html = """
        <div class="product-card">
            <div class="product-title">Test Product 1</div>
            <div class="product-price">₹499</div>
            <img src="http://example.com/image1.jpg" />
        </div>
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = mock_html

        scraper = Scraper("http://example.com")
        products = scraper.scrape_page(page_number=1)

        self.assertEqual(len(products), 1)
        self.assertEqual(products[0]["product_title"], "Test Product 1")
        self.assertEqual(products[0]["product_price"], 499.0)
        self.assertEqual(products[0]["path_to_image"],
                         "http://example.com/image1.jpg")

    @patch("app.services.scraper.requests.get")
    def test_scrape_page_failure(self, mock_get):
        """
        Test that scrape_page handles HTTP errors gracefully.
        """
        mock_get.return_value.status_code = 500
        scraper = Scraper("http://example.com")
        products = scraper.scrape_page(page_number=1)
        self.assertEqual(products, [])

    @patch("app.services.scraper.requests.get")
    def test_scrape_all(self, mock_get):
        """
        Test that scrape_all calls scrape_page for each page.
        """
        mock_html = """
        <div class="product-card">
            <div class="product-title">Test Product 2</div>
            <div class="product-price">₹999</div>
            <img src="http://example.com/image2.jpg" />
        </div>
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = mock_html

        scraper = Scraper("http://example.com")
        products = scraper.scrape_all(limit=2)

        self.assertEqual(len(products), 2)
        self.assertEqual(products[0]["product_title"], "Test Product 2")
        self.assertEqual(products[1]["product_title"], "Test Product 2")


if __name__ == "__main__":
    unittest.main()
