from bs4 import BeautifulSoup
import requests

# Define URL
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "lxml")

    # Access header tag
    header_tag = soup.header
    print("Header Tag:")
    print(header_tag)

    # Access div tag
    div_tag = soup.div
    print("Div Tag:")
    print(div_tag)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
