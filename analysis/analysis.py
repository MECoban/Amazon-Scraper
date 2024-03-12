import pandas as pd
import numpy as np

usa_products_df = pd.read_csv("data/home-kitchen_feature_usa.csv")
ca_products_df = pd.read_csv("data/home-kitchen_feature_ca.csv")

products_df = usa_products_df.drop_duplicates(subset="ASIN", keep="first")
products_df1 = ca_products_df.drop_duplicates(subset="ASIN", keep="first")

products_df.to_csv("data/feature_usa.csv", index=False)
products_df1.to_csv("data/feature_ca.csv", index=False)

usa_df = pd.read_csv("data/feature_usa.csv")
canada_df = pd.read_csv("data/feature_ca.csv")

usa_df["Price"] = pd.to_numeric(
    usa_df["Price"].replace("[\$,]", "", regex=True).replace("Price not found", np.nan),
    errors="coerce",
)
canada_df["Price"] = pd.to_numeric(
    canada_df["Price"]
    .replace("[\$,]", "", regex=True)
    .replace("Price not found", np.nan),
    errors="coerce",
)

merged_df = pd.merge(usa_df, canada_df, on="ASIN", suffixes=("_USA", "_Canada"))


merged_df["Profit($)"] = (
    merged_df["Price_Canada"] - merged_df["Price_USA"]
)  # Calculation potential profit for each product
merged_df["Profit($)"] = merged_df["Profit($)"].round(2)
merged_df["Profit_Percentage(%)"] = (
    merged_df["Profit($)"] / merged_df["Price_USA"] * 100
)
merged_df["Profit_Percentage(%)"] = merged_df["Profit_Percentage(%)"].round(2)


profitable_products = merged_df[merged_df["Profit($)"] > 0]
profitable_products = profitable_products[
    [
        "ASIN",
        "URL_USA",
        "URL_Canada",
        "Price_USA",
        "Price_Canada",
        "Profit($)",
        "Profit_Percentage(%)",
    ]
]
profitable_products.sort_values(
    by="Profit_Percentage(%)", ascending=False, inplace=True
)
profitable_products.to_csv("profitable_products.csv", index=False)
