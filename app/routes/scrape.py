from fastapi import APIRouter, Depends, HTTPException
from app.services.scraper import Scraper
from app.services.storage import JSONStorage
from app.services.notifier import ConsoleNotifier
from app.services.cache import Cache
from app.config import API_TOKEN

router = APIRouter()

# Dependency for token authentication


def authenticate(token: str):
    if token != API_TOKEN:
        raise HTTPException(status_code=403, detail="Unauthorized")


@router.post("/scrape/")
def scrape(limit: int, proxy: str = None, token: str = Depends(authenticate)):
    print(f"DEBUG: Received limit={limit}, proxy={proxy}, token={token}")
    return {"status": "success", "products_scraped": 0}
    """
    Endpoint to start the scraping process.

    Parameters:
    - limit: Maximum number of pages to scrape.
    - proxy: Optional proxy string for scraping.
    - token: Authentication token.

    Returns:
    - Dictionary with scraping status and product count.
    """
    scraper = Scraper("https://dentalstall.com/shop/")
    storage = JSONStorage("data/scraped_data.json")
    notifier = ConsoleNotifier()
    cache = Cache()

    # Scrape data
    data = scraper.scrape_all(limit, proxy)
    updated_count = 0

    # Save and check for updates
    for item in data:
        if cache.get(item["product_title"]) == item["product_price"]:
            continue
        cache.set(item["product_title"], item["product_price"])
        updated_count += 1

    storage.save(data)
    notifier.notify(f"Scraped and updated {updated_count} products.")
    return {"status": "success", "products_scraped": len(data)}
