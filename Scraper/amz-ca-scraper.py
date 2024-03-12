from requests_html import HTMLSession
import pandas as pd
import time
import random

main_url = "https://www.amazon.ca/s?i=kitchen&rh=n%3A2206275011&fs=true&"
num_pages = 350

s = HTMLSession()

asins = []
titles = []
urls = []
prices = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',  # Replace with a user agent string
    'Accept-Language': 'en-US,en;q=0.9',
}

for p_num in range(1, num_pages + 1):
    page_url = f"{main_url}page={p_num}"
    print(f"Processing {page_url}")
    try:
        r = s.get(page_url, headers=headers)
        r.html.render(sleep=random.uniform(5, 8))  # Randomized sleep to mimic human behavior
        items = r.html.find("div[data-asin]")

        for item in items:
            asin = item.attrs.get("data-asin", None)
            if asin:
                asins.append(asin)
                urls.append(f"https://www.amazon.ca/dp/{asin}")
                
                # Assuming these are the correct selectors
                title_selector = "span.a-size-medium.a-color-base.a-text-normal"
                price_selector = "span.a-price > span.a-offscreen"
                
                title_element = item.find(title_selector, first=True)
                titles.append(title_element.text if title_element else "Title not found")

                price_element = item.find(price_selector, first=True)
                prices.append(price_element.text if price_element else "Price not found")

    except Exception as e:
        print(f"An error occurred on page {p_num}: {e}")

    time.sleep(random.uniform(3, 9))  # Sleep after each page request

# Verify data consistency
if len(asins) == len(titles) == len(urls) == len(prices):
    products_df = pd.DataFrame({
        "ASIN": asins,
        "Title": titles,
        "URL": urls,
        "Price": prices
    })
    try:
        products_df.to_csv("data/home-kitchen_feature_ca.csv", index=False)
        print("CSV file has been saved.")
    except Exception as e:
        print(f"Error saving CSV: {e}")
else:
    print("Mismatch in list lengths, please check the scraped data.")
