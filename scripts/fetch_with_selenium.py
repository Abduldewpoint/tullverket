from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Start headless Chrome browser
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

# Open the page
driver.get("https://tulltaxan.tullverket.se/arctictariff-public-web/#!/taric/moreinfo/codelists/search")
print("🔁 Waiting for the page to load...")
time.sleep(5)

# Find dropdown (adjust ID or logic if needed)
dropdown = driver.find_element(By.ID, "codeType")
dropdown.click()
time.sleep(1)

# Choose a specific code list (e.g., Typ av deklaration)
option = driver.find_element(By.XPATH, "//option[contains(text(), 'Typ av deklaration')]")
option.click()
time.sleep(1)

# Click search button
search_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Sök')]")
search_btn.click()
time.sleep(5)

# Save HTML content
with open("typ_av_deklaration.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)

print("✅ HTML file saved as typ_av_deklaration.html")

driver.quit()
