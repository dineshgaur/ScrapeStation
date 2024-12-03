# ScrapeStation

**ScrapeStation** is a web scraping tool built with **FastAPI**. It automates the scraping of product data from e-commerce websites and supports caching, notifications, and extensible storage mechanisms. The project is modular, scalable, and designed with object-oriented principles.

---

## Features

- **Scraping**: Extracts product title, price, and image URL.
- **Page Limit**: Allows setting a maximum number of pages to scrape.
- **Proxy Support**: Enables proxy usage for scraping.
- **Caching**: Uses Redis to prevent redundant updates for unchanged data.
- **Notifications**: Notifies scraping status and results.
- **Storage**: Saves data in JSON format with extensibility for other storage backends.

---

## Tech Stack

- **Framework**: FastAPI
- **Web Scraping**: BeautifulSoup, Requests
- **Caching**: Redis
- **Data Storage**: JSON
- **Programming Language**: Python
