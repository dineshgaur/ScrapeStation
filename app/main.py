from app.routes.scrape import router as scrape_router
from fastapi import FastAPI
import sys
import os

# Add the project root directory to sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)


app = FastAPI(
    title="ScrapeStation",
    description="A FastAPI-based web scraper tool with caching and notifications.",
    version="1.0.0"
)

# Register routes
app.include_router(scrape_router, prefix="/api", tags=["Scraping"])


@app.get("/")
def read_root():
    return {"message": "Welcome to ScrapeStation! Use /api/scrape to start scraping."}
