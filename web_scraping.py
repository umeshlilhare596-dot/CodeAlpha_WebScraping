import requests
from bs4 import BeautifulSoup
import csv

# Public website for web scraping practice
url = "https://books.toscrape.com/"

# Send request to website
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    print("Website accessed successfully!")

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")

    # Create CSV file
    with open("books_dataset.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["Book Title", "Price", "Availability"])

        # Extract data
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            availability = book.find(
                "p", class_="instock availability"
            ).text.strip()

            writer.writerow([title, price, availability])

    print("Data extracted successfully!")
    print("Dataset saved as books_dataset.csv")

else:
    print("Failed to access website.")
