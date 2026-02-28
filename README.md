# Books Scraper

A web scraper built with Scrapy to collect book data from books.toscrape.com.

## Data Collected
- Title
- Price
- Star Rating
- Stock Status

## Tech Stack
- Python
- Scrapy

## How to Run
1. Clone this repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install scrapy`
5. Run spider: `scrapy crawl bookspider -o books.csv`
