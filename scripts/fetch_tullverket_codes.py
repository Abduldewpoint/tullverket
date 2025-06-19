import requests
import pandas as pd
from datetime import datetime

# Step 1: Set the API endpoint
url = "https://tulltaxan.tullverket.se/arctictariff-public-proxy/arctictariff-trusted-rs/v1/cl/codetypes"

# Step 2: Set the parameters for the request
params = {
    "codetype": "1101000000,GCR",       # This is the code type for "Typ av deklaration"
    "startDate": "2024-12-31",          # Use a working date (adjust if needed)
    "endDate": "2024-12-31",
    "language": "en",                   # Language of the returned data
    "sortOrder": "A"                    # Sort ascending
}

# Step 3: Set headers to make the request look like a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en;q=0.9,nl;q=0.8,nl-NL;q=0.7,en-US;q=0.6,ar;q=0.5",
    "Referer": "https://tulltaxan.tullverket.se/arctictariff-public-web/",
    "Origin": "https://tulltaxan.tullverket.se"
    # You can also add "Cookie": "..." if the API requires a session cookie
}

# Step 4: Send the GET request
response = requests.get(url, params=params, headers=headers)

# Step 5: Print some debug info
print("Status code:", response.status_code)
print("Request URL:", response.url)
print("First part of the response:", response.text[:300])

# Step 6: Check if response is OK
if response.status_code == 200:
    try:
        # Step 7: Convert JSON response to Python dict
        data = response.json()

        # Step 8: Check if the response contains a list of codes
        if "codeList" in data:
            # Step 9: Convert list to DataFrame and save as CSV
            df = pd.DataFrame(data["codeList"])
            today = datetime.today().strftime('%Y-%m-%d')
            filename = f"typ_av_deklaration_{today}.csv"
            df.to_csv(filename, index=False)
            print("✅ File saved:", filename)
        else:
            print("⚠️ 'codeList' not found in the response.")
    except Exception as e:
        print("❌ Error while reading JSON:", e)
else:
    print("❌ API request failed with status code:", response.status_code)
