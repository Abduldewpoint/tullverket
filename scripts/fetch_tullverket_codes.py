# This script gets "Typ av deklaration" codes from Tullverket API
import requests
import pandas as pd
from datetime import datetime

# Step 1: Set API URL and parameters
url = "https://tulltaxan.tullverket.se/arctictariff-public-proxy/arctictariff-trusted-rs/v1/cl/codetypes"

params = {
    "codetype": "1101000000,GCR",   # Typ av deklaration
    "startDate": "2024-12-31",      # Use a known working date
    "endDate": "2024-12-31",
    "language": "en",
    "sortOrder": "A"
}

# Step 2: Call the API
response = requests.get(url, params=params)

# Step 3: Show status and debug info
print("Status code:", response.status_code)
print("URL:", response.url)
print("First 300 characters of response:")
print(response.text[:300])

# Step 4: Check if response is OK
if response.status_code != 200 or not response.text.strip():
    print("❌ API did not return valid data.")
    exit(1)

# Step 5: Try to load the JSON
try:
    data = response.json()
except Exception as e:
    print("❌ Error reading JSON:", e)
    exit(1)

# Step 6: Check and save the code list
if "codeList" in data:
    df = pd.DataFrame(data["codeList"])
    today = datetim
