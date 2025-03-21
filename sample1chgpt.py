from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open Google
driver.get("https://www.google.com")

# Find the search box, type query & hit Enter
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(3)

# Print the search result titles
results = driver.find_elements(By.CSS_SELECTOR, "h3")
for index, result in enumerate(results[:5]):  # Print first 5 results
    print(f"{index+1}. {result.text}")

# Close the browser
driver.quit()
