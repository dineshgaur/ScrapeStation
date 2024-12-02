from fastapi import FastAPI
from app.routes.scrape import router as scrape_router

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
