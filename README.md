# Amazon Profitable Product Finder For Dropshipping and Arbitrage 

## Overview
This suite of Python scripts scrapes Amazon Canada and Amazon USA for products in the home and kitchen category, compares the prices, and identifies 
profitable arbitrage opportunities based on price differences.

## Requirements
Python 3
Libraries: requests_html, pandas
To install the required Python libraries, run:

```
pip install requests_html pandas
```


Files
home-kitchen_feature_usa.csv / home-kitchen_feature_ca.csv: Raw data scraped from Amazon USA/Canada.
feature_usa.csv / feature_ca.csv: De-duplicated product lists for USA/Canada.
profitable_products.csv: Final output listing products with potential profit.

## Running the Script
Update main_url in the script to the desired Amazon category page.
Set num_pages to the number of pages you wish to scrape.

Execute the scraping scripts for each region:

```
python amazon_scrape_usa.py
```

```
python amazon_scrape_ca.py
```
Run the comparison and profit calculation:

```
python analysis.py
```

## How It Works

The scripts make HTTP requests to Amazon's search results pages and parse the HTML to extract product details. 
Then they merge the USA and Canada product data on their ASINs, calculate the price difference, and output products 
that are cheaper in the USA compared to Canada, along with the profit percentage.

<img width="1366" alt="Screenshot " src="https://github.com/MECoban/Amazon-Scraper/assets/156511598/5612057e-c8da-4a55-8002-099c81cfb49e">

## Troubleshooting

Ensure you have a stable internet connection.
Amazon may block requests if too many are made in a short time; use delays between requests.

## Disclaimer

This tool is intended for educational purposes only. Always adhere to Amazon’s Terms of Service. 
Automated scraping and price comparison may be against their terms and could result in account penalties. Use responsibly. 
Be aware: Shipping fee and Amazon selling commisions not included. 
