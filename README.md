# Web Scraping Workshop

A hands-on Python workshop: scrape book titles and prices from [books.toscrape.com](https://books.toscrape.com) and export them to a CSV file.

## Setup

**Python 3.8+ required.**

Install dependencies:

```bash
pip install requests beautifulsoup4
```

## Your Task

Open [scraper_starter.py](scraper_starter.py) and complete the **8 TODOs**:

| TODO | What you'll implement |
|------|-----------------------|
| 1 | Send an HTTP GET request |
| 2 | Handle request errors |
| 3 | Parse HTML with BeautifulSoup |
| 4 | Find all book elements on a page |
| 5 | Extract each book's title |
| 6 | Extract each book's price |
| 7 | Loop over multiple pages (pagination) |
| 8 | Write results to a CSV file |

When finished, run:

```bash
python scraper_starter.py
```

Expected output:
```
Starting scraper...
Scraping page 1 ...
Scraping page 2 ...
...
Total books scraped: 50
  £51.77  A Light in the Attic
  ...
Saved 50 books to books.csv
```

## Tips

- Use your browser's **DevTools → Inspector** (F12) to explore the HTML structure of books.toscrape.com before writing any selectors.
- Each book lives inside an `<article class="product_pod">` element.
- The page URL pattern is `https://books.toscrape.com/catalogue/page-{N}.html`.

## Ethics & Limitations

- Always check a site's `robots.txt` before scraping.
- Add delays between requests on real sites to avoid overloading servers.
- Scrapers break when the site's HTML structure changes — this is intentional in the debugging activity!
