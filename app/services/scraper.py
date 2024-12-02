import requests
from bs4 import BeautifulSoup
from time import sleep


class Scraper:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def scrape_page(self, page_number: int, proxy: str = None):
        """
        Scrapes a single page for product data.

        Args:
        - page_number: The page number to scrape.
        - proxy: Optional proxy string for the request.

        Returns:
        - A list of dictionaries containing product details.
        """
        url = f"{self.base_url}?page={page_number}"
        try:
            response = requests.get(
                url, proxies={"http": proxy, "https": proxy}, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            products = []

            # Assuming product cards have specific classes (adjust selectors based on actual HTML structure)
            for product in soup.select(".product-card"):
                title = product.select_one(".product-title").text.strip()
                price = float(product.select_one(
                    ".product-price").text.strip().replace("₹", "").replace(",", ""))
                image_url = product.select_one("img")["src"]

                products.append({
                    "product_title": title,
                    "product_price": price,
                    "path_to_image": image_url,
                })

            return products
        except requests.RequestException as e:
            print(f"Error scraping page {page_number}: {e}")
            return []

    def scrape_all(self, limit: int, proxy: str = None):
        """
        Scrapes multiple pages up to the specified limit.

        Args:
        - limit: Number of pages to scrape.
        - proxy: Optional proxy string for the requests.

        Returns:
        - A list of dictionaries containing product details.
        """
        all_products = []
        for page in range(1, limit + 1):
            print(f"Scraping page {page}...")
            products = self.scrape_page(page, proxy)
            all_products.extend(products)
            sleep(1)  # Add delay to prevent overloading the target server
        return all_products
