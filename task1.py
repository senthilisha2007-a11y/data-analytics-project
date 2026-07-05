import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Check request
if response.status_code == 200:
    print("Website Connected Successfully!\n")
else:
    print("Connection Failed!")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote blocks
quotes = soup.find_all("div", class_="quote")

# Store data
quote_list = []
author_list = []
tag_list = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    tags = quote.find_all("a", class_="tag")
    tag_text = ", ".join([tag.text for tag in tags])

    quote_list.append(text)
    author_list.append(author)
    tag_list.append(tag_text)

# Create DataFrame
data = pd.DataFrame({
    "Quote": quote_list,
    "Author": author_list,
    "Tags": tag_list
})

# Display Output
print(data)

# Save CSV
data.to_csv("quotes_dataset.csv", index=False)

print("\nDataset Saved Successfully as quotes_dataset.csv")