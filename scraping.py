import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver

# URL of the product page
url = 'https://www.flipkart.com/womens-footwear/flats/pr?sid=iko%2C9d5'

# Start the webdriver
driver = webdriver.Firefox()  # or webdriver.Chrome()

# Load the webpage
driver.get(url)

# Get the HTML content
html = driver.page_source

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Extract product details
name = soup.find('h1', class_='product-title')
if name and name.text:
    name = name.text.strip()
else:
    name = ""

price = soup.find('div', class_='price')
if price and price.text:
    price = price.text.strip()
else:
    price = ""

rating = soup.find('span', class_='rating')
if rating and rating.text:
    rating = rating.text.strip()
else:
    rating = ""

reviews = soup.find('span', class_='reviews')
if reviews and reviews.text:
    reviews = reviews.text.strip()
else:
    reviews = ""

description = soup.find('div', class_='product-description')
if description and description.text:
    description = description.text.strip()
else:
    description = ""

# Write data to CSV file
with open('product_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, price, rating, reviews, description])

print("Product Data:")
print("Name:", name)
print("Price:", price)
print("Rating:", rating)
print("Reviews:", reviews)
print("Description:", description)

# Don't forget to close the webdriver
driver.quit()
