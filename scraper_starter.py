"""
Web Scraping Workshop — Starter Code
Target site: https://books.toscrape.com

Before you begin, install the two libraries we need:
    pip install requests beautifulsoup4

Goal: Scrape book titles and prices from books.toscrape.com
      across multiple pages and save the results to a CSV file.

How to use this file:
    - Find each TODO comment and fill in the missing code.
    - Run the script with:  python scraper_starter.py
"""

import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/catalogue/"


# ── Helper ────────────────────────────────────────────────────────────────────

def get_page(url):
    """Fetch a page and return a BeautifulSoup object."""

    # TODO 1 ── Send an HTTP GET request to `url`
    # Use the requests library to make a GET request, just like a browser would.
    # Store the result in a variable called `response`.
    # Hint: requests.get() is the method you need. Pass the URL as an argument.
    response = None  # ← replace this line

    # TODO 2 ── Check that the request succeeded
    # Call a method on `response` that raises an error if the server
    # returned a failure code (like 404 or 500).
    # Hint: response.raise_for_status() is a convenient way to do this.

    # TODO 3 ── Parse the HTML and return the result
    # Use BeautifulSoup to turn response.text (the raw HTML string) into
    # a searchable object. You'll need to specify a parser: "html.parser".
    # Hint: BeautifulSoup() is the constructor you need. Pass the HTML and parser as arguments.
    return None  # ← replace this line


# ── Extraction ────────────────────────────────────────────────────────────────

def extract_books(soup):
    """Return a list of (title, price) tuples from a single page."""
    books = []

    # TODO 4 ── Find all book elements on the page
    # Open https://books.toscrape.com, press F12, and use the inspector
    # to click on a book. Each book is wrapped in a specific HTML tag with
    # a class name — find it, then use soup.find_all() to get all of them.
    # Hint: Look for <article class="product_pod"> in the HTML structure. This is the tag that contains each book's info.
    book_elements = []  # ← replace this line

    for book in book_elements:

        # TODO 5 ── Extract the title
        # Inspect the book element in DevTools. The full title is stored as
        # an HTML *attribute* on an <a> tag (not the visible link text).
        # Use .find() to navigate to the right tag and read that attribute.
        # Hint: The title is in the <a> tag inside the <h3> tag. You can access it with book.find("h3").find("a")["title"].
        title = ""  # ← replace this line

        # TODO 6 ── Extract the price
        # The price is the text content of a tag with a specific class name.
        # Find the tag by its class, then read its .text property.
        # Hint: The price is in a tag with class "price_color". You can access it with book.find(class_="price_color").text.
        price = ""  # ← replace this line

        books.append((title, price))

    return books


# ── Pagination ────────────────────────────────────────────────────────────────

def scrape_all_pages(num_pages=5):
    """Scrape `num_pages` pages and return all (title, price) tuples."""
    all_books = []

    # TODO 7 ── Loop over pages and collect all books
    # Page URLs follow this pattern:
    #   https://books.toscrape.com/catalogue/page-1.html
    #   https://books.toscrape.com/catalogue/page-2.html  … and so on.
    #
    # For each page number from 1 to num_pages:
    #   - Build the URL using BASE_URL and an f-string
    #   - Print a short status message so you can see progress
    #   - Call get_page() and extract_books()
    #   - Add the results to all_books (hint: look up list.extend())
    # Hint: Use a for loop with range(1, num_pages + 1) to iterate through page numbers.

    return all_books


# ── Export ────────────────────────────────────────────────────────────────────

def save_to_csv(books, filename="books.csv"):
    """Write the list of (title, price) tuples to a CSV file."""

    # TODO 8 ── Write the results to a CSV file
    # Use Python's built-in csv module (already imported above).
    # Open the file in write mode — pass newline="" to avoid extra blank
    # rows on Windows, and encoding="utf-8" for special characters.
    # Write a header row first: ["Title", "Price"]
    # Then write all the book rows at once.
    # Hint: Use csv.writer() to create a writer object, then call writer.writerow() for the header and writer.writerows() for the book data.

    with open(filename, "w", newline="", encoding="utf-8") as f:
        pass  # TODO 8 ← replace `pass` with your csv.writer code

    print(f"Saved {len(books)} books to {filename}")


# ── Main ──────────────────────────────────────────────────────────────────────
# Run `python scraper_starter.py` after completing each group of TODOs.
# The script checks your progress and stops at the first unfinished stage.

if __name__ == "__main__":

    # ── Stage 1: get_page()  (TODOs 1-3) ─────────────────────────────────────
    print("── Stage 1: get_page() ──────────────────────────────────")
    soup = get_page(BASE_URL + "page-1.html")
    if soup is None:
        print("  ✗  get_page() returned None — complete TODOs 1-3 first.")
        exit()
    print(f"  ✓  Page fetched! Page title: {soup.title.text.strip()}\n")

    # ── Stage 2: extract_books()  (TODOs 4-6) ────────────────────────────────
    print("── Stage 2: extract_books() ─────────────────────────────")
    books_page1 = extract_books(soup)
    if not books_page1:
        print("  ✗  extract_books() returned nothing — complete TODOs 4-6 first.")
        exit()
    print(f"  ✓  Found {len(books_page1)} books on page 1. First 3:")
    for title, price in books_page1[:3]:
        print(f"       {price}  {title}")
    print()

    # ── Stage 3: scrape_all_pages()  (TODO 7) ────────────────────────────────
    print("── Stage 3: scrape_all_pages() ──────────────────────────")
    all_books = scrape_all_pages(num_pages=5)
    if not all_books:
        print("  ✗  scrape_all_pages() returned nothing — complete TODO 7 first.")
        exit()
    print(f"  ✓  Total books scraped: {len(all_books)}\n")

    # ── Stage 4: save_to_csv()  (TODO 8) ─────────────────────────────────────
    print("── Stage 4: save_to_csv() ───────────────────────────────")
    save_to_csv(all_books)
    import os
    if os.path.getsize("books.csv") > 0:
        print("  ✓  books.csv written successfully!")
    else:
        print("  ✗  books.csv is empty — complete TODO 8 first.")
