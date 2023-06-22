# Amazon Price Comparison Algorithm

This is a Python program that compares prices of products from Amazon.sg. It retrieves the product details and prices from the provided URLs and displays the lowest price along with its corresponding URL.

## How to Set Up

To set up and run this program, follow the steps below:

1. Install Python: Make sure you have Python installed on your system. You can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Install Required Libraries: Open a terminal or command prompt and execute the following command to install the necessary libraries:
`pip install requests beautifulsoup4`

3. Copy the Code: Copy the entire code from the code snippet provided.

4. Run the Program: Open a text editor or an Integrated Development Environment (IDE) of your choice, paste the code, and save the file with a `.py` extension (e.g., `scraper.py`).

5. Provide Product URLs: Modify the `product_urls` list in the code to include the URLs of the products you want to compare. You can add or remove URLs as needed.

6. Run the Script: Open a terminal or command prompt, navigate to the directory where you saved the script, and execute the following command:
`python scraper.py`



The program will start running and display the product titles, prices, and the lowest price with its corresponding URL.

## What the Program is Doing

This program utilizes the `requests` and `BeautifulSoup` libraries to scrape product details and prices from the provided Amazon.sg URLs. It compares the prices of the products and identifies the lowest price among them.

Here's an overview of the program's functionality:

1. The program imports the necessary libraries: `requests`, `BeautifulSoup`, and `locale`. The `locale` library is used to format currency values.

2. The `get_product_details(url)` function takes a URL as input, sends a GET request to the URL with a custom User-Agent header, and retrieves the HTML content of the page. It then uses `BeautifulSoup` to parse the HTML and extract the product title and price.

3. The `compare_prices(product_urls)` function takes a list of product URLs as input. It iterates over each URL, calls the `get_product_details()` function to retrieve the product details, and stores the title and price in a dictionary.

4. After retrieving all the prices, the program finds the lowest price among them and identifies the corresponding URL.

5. Finally, the program displays the product titles, formatted prices, and the URL of the product with the lowest price.

Please note that this program assumes the structure of the Amazon.sg HTML pages and may require modifications if the structure or elements change in the future.

Feel free to customize the program and add more functionalities according to your requirements.

