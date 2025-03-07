# -*- coding: utf-8 -*-
"""cryptocurrency.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ovk-e01anQy2V_UQHKA6emmg_PDZ8Vpw
"""

!pip install openpyxl

import requests
import pandas as pd

# Function to fetch top 50 cryptocurrency data
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,  # Fetch top 50 cryptocurrencies
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Extract required fields
    crypto_list = []
    for coin in data:
        crypto_list.append([
            coin["name"],         # Cryptocurrency Name
            coin["symbol"].upper(),  # Symbol
            coin["current_price"],   # Current Price (USD)
            coin["market_cap"],      # Market Capitalization
            coin["total_volume"],    # 24-hour Trading Volume
            coin["price_change_percentage_24h"]  # 24h Price Change (%)
        ])

    # Convert to Pandas DataFrame
    columns = ["Name", "Symbol", "Current Price (USD)", "Market Cap", "24h Volume", "24h % Change"]
    df = pd.DataFrame(crypto_list, columns=columns)

    return df

# Fetch and display data
crypto_df = fetch_crypto_data()
crypto_df.head()

# Identify the top 5 cryptocurrencies by market cap
top_5_crypto = crypto_df.sort_values(by="Market Cap", ascending=False).head(5)

# Calculate the average price of the top 50 cryptocurrencies
average_price = crypto_df["Current Price (USD)"].mean()

# Find highest and lowest 24h percentage change
highest_change = crypto_df.loc[crypto_df["24h % Change"].idxmax()]
lowest_change = crypto_df.loc[crypto_df["24h % Change"].idxmin()]

# Print results
print("Top 5 Cryptocurrencies by Market Cap:\n", top_5_crypto)
print("\nAverage Price of Top 50 Cryptos: $", round(average_price, 2))
print("\nHighest 24h % Change:", highest_change["Name"], highest_change["24h % Change"])
print("Lowest 24h % Change:", lowest_change["Name"], lowest_change["24h % Change"])

from openpyxl import Workbook

# Save DataFrame to an Excel file
excel_filename = "cryptodata.xlsx"
crypto_df.to_excel(excel_filename, index=False)

print(f"Data saved to {excel_filename}")

import time

while True:
    crypto_df = fetch_crypto_data()
    crypto_df.to_excel(excel_filename, index=False)
    print(f"Updated data saved at {pd.Timestamp.now()}")

    # Wait for 5 minutes (300 seconds)
    time.sleep(300)