import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get the HTML content of a page
def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve page: {response.status_code}")
        return None

# Function to parse the HTML and extract product information
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    
    # Finding all product listings
    for item in soup.find_all('article', class_='product_pod'):
        # Extracting the product name
        name = item.h3.a['title']
        
        # Extracting the product price
        price = item.find('p', class_='price_color').text.strip()
        
        # Extracting the rating (as class value) and converting it to a number
        rating = item.p['class'][1]
        rating_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        rating = rating_dict.get(rating, 'No rating')
        
        # Appending the product info to the list
        products.append({'Name': name, 'Price': price, 'Rating': rating})
    
    return products

# Function to save the product information to a CSV file
def save_to_csv(products, filename):
    df = pd.DataFrame(products)
    df.to_csv(filename, index=False)
    print(f"Saved {len(products)} products to {filename}")

# Main function to scrape the website and save the data
def main():
    url = 'http://books.toscrape.com/catalogue/category/books_1/index.html'
    html = get_html(url)
    
    if html:
        products = parse_html(html)
        save_to_csv(products, 'books.csv')

if __name__ == '__main__':
    main()
