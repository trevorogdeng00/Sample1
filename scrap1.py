from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Define the target URL
url = "https://example.com"
driver.get(url)

# Wait for the page to load
time.sleep(2)

# Extract data using XPath or CSS selectors
try:
    title = driver.find_element(By.XPATH, "//h1").text
    description = driver.find_element(By.CSS_SELECTOR, ".description").text
    print(f"Title: {title}")
    print(f"Description: {description}")
except Exception as e:
    print(f"Error: {e}")

# Close the browser
driver.quit()