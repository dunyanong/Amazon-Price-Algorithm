import requests
from bs4 import BeautifulSoup
import locale

product_urls = [
    'https://www.amazon.sg/dp/B07TWFWJDZ/ref=s9_acsd_al_bw_c2_x_3_i?pf_rd_m=ACT6OAM3OSC9S&pf_rd_s=merchandised-search-3&pf_rd_r=1Z78690TJ67CMVW8P0P5&pf_rd_t=101&pf_rd_p=27e63ee9-0faa-42a6-a4ff-c85e38ec1055&pf_rd_i=6436080051',
    'https://www.amazon.sg/Oculus-Quest-Advanced-All-One/dp/B09B8DQ26F?ref_=Oct_d_omwf_m_6436080051_1&pd_rd_w=0OjT4&content-id=amzn1.sym.615a6dd0-570e-4011-b6c6-61582e4e11d6&pf_rd_p=615a6dd0-570e-4011-b6c6-61582e4e11d6&pf_rd_r=MMXX8VHMPPCR9PRC9AWJ&pd_rd_wg=QtCQ2&pd_rd_r=c3c52eeb-2269-4533-b526-b2a0d17adbcf&pd_rd_i=B09B8DQ26F'
]

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

def get_product_details(url):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text().strip()
    price = soup.select_one('.a-price-whole').get_text().strip()

    return title, price

def compare_prices(product_urls):
    prices = {}

    for url in product_urls:
        try:
            title, price = get_product_details(url)
            prices[url] = {'title': title, 'price': price}
        except Exception as e:
            print(f"Failed to retrieve data for {url}. Error: {str(e)}")

    lowest_price = float('inf')
    lowest_price_url = None

    for url, data in prices.items():
        title = data['title']
        price = float(data['price'].replace(',', ''))
        print("Title:", title)
        formatted_price = locale.currency(price, grouping=True)  # Format price with commas
        print("Price:", formatted_price)
        print("-----------------------")

        if price < lowest_price:
            lowest_price = price
            lowest_price_url = url

    if lowest_price_url:
        formatted_lowest_price = locale.currency(lowest_price, grouping=True)  # Format lowest price with commas
        print(f"The lowest price is {formatted_lowest_price} at the following URL:")
        print(lowest_price_url)
    else:
        print("No prices found.")

# Set the locale for formatting currency
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

compare_prices(product_urls)