from requests_html import HTMLSession
import pandas as pd


main_url = "https://www.amazon.com/s?i=kitchen-intl-ship&rh=n%3A16225011011&fs=true&"
num_pages = 300


s = HTMLSession()


asins = []
titles = []
urls = []
prices = []
# dimensions = []


for p_num in range(1, num_pages + 1):
    page_url = f"{main_url}page={p_num}"
    r = s.get(page_url)
    r.html.render(sleep=1, timeout=30)  # Increase timeout if necessary
    print(f"Processing {page_url}")

    items = r.html.find("div[data-asin]")

    for item in items:
        asin = item.attrs["data-asin"]
        if asin:
            asins.append(asin)
            product_url = f"https://www.amazon.com/dp/{asin}"
            urls.append(product_url)

            title_element = item.find("span.a-text-normal", first=True)
            if title_element:
                titles.append(title_element.text)
            else:
                titles.append(None)

            # titles.append(title_element.text if title_element else None)

            price_element = item.find("span.a-price > span.a-offscreen", first=True)
            if price_element:
                prices.append(price_element.text)
            else:
                prices.append(None)

            # prices.append(price_element.text if price_element else None)

            """product_page = s.get(product_url)
            product_page.html.render(sleep=1, timeout=30)  # Increase sleep time if necessary to ensure the page loads completely
            product_details = product_page.html.find('#detailBullets_feature_div', first=True)  # Target the container that usually holds details
            if product_details:
                # Look for a list item that contains the dimensions
                dimension_elements = product_details.find('li')
                dimension_text = None
                for element in dimension_elements:
                    if 'Product Dimensions' in element.text:
                        dimension_text = element.text.split('\n')[-1]  # The actual dimensions are usually after the label
                        break
                dimensions.append(dimension_text)
            else:
                dimensions.append(None)"""

# Check that all lists are the same length
assert (
    len(asins) == len(titles) == len(urls) == len(prices)
), "Mismatch in list lengths"  # for dimensions add == len(dimensions)


products_df = pd.DataFrame(
    {
        "ASIN": asins,
        "Title": titles,
        "URL": urls,
        "Price": prices,
        # "Dimensions": dimensions
    }
)

# Print the DataFrame to verify if you need
# print(products_df)

products_df.to_csv("data/home-kitchen_feature_usa.csv", index=False)
