from pydantic import BaseModel, Field
from typing import Optional


class ScrapeRequest(BaseModel):
    """
    Model for validating scraping requests.
    """
    limit: int = Field(..., gt=0,
                       description="Number of pages to scrape (must be greater than 0).")
    proxy: Optional[str] = Field(
        None, description="Proxy string for scraping (optional).")


class ScrapedProduct(BaseModel):
    """
    Model for representing a single scraped product.
    """
    product_title: str = Field(..., description="The title of the product.")
    product_price: float = Field(..., ge=0,
                                 description="The price of the product (must be non-negative).")
    path_to_image: str = Field(...,
                               description="The path to the product image.")
