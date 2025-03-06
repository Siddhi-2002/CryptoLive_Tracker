# CryptoLive_Tracker
A Python-based live cryptocurrency data tracker with real-time Excel updates.

# Google Sheets Setup  

# Required Columns  
Ensure your Google Sheet has the following columns in the exact order:  

| Column Name           | Description |
|-----------------------|------------|
| `Timestamp`          | The date and time of the entry (automatically recorded). |
| `Name`               | The name of the cryptocurrency. |
| `Symbol`             | The ticker symbol (e.g., BTC, ETH). |
| `Current Price (USD)` | The latest price in USD. |
| `Market Cap`         | The total market capitalization of the cryptocurrency. |
| `24h Volume`         | The total trading volume in the last 24 hours. |
| `24h % Change`       | The percentage change in price over the last 24 hours. |

# Permissions Needed  
To allow the script to update the sheet, ensure:  
- You have edit access to the Google Sheet.  
- If the script is deployed as a web app, grant permission to access and modify the sheet when prompted.  

# How to Link Your Google Sheet  
1. Open your Google Sheet and copy its Sheet ID from the URL:  
   ```
   https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit
   ```
2. Paste the Sheet ID into the script where required.  
