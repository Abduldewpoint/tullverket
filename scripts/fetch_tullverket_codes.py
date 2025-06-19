import requests
import pandas as pd
from datetime import datetime

# API URL and parameters for Landkod
url = "https://tulltaxan.tullverket.se/arctictariff-public-proxy/arctictariff-trusted-rs/v1/cl/codetypes"
params = {
    "codetype": "1101000000,GCR",  # Typ av deklaration
    "startDate": "2025-06-19",
    "endDate": "2025-06-19",
    "language": "en",
    "sortOrder": "A"
}

# API call
response = requests.get(url, params=params)
data = response.json()

# Save to CSV if data found
if 'codeList' in data:
    df = pd.DataFrame(data['codeList'])
    today = datetime.today().strftime('%Y-%m-%d')
    filename = f"tullverket_codes_{today}.csv"
    df.to_csv(filename, index=False)
    print("✅ File saved:", filename)
else:
    print("❌ No data found.")
