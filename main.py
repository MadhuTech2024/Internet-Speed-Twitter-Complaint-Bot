import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Load credentials from .env
load_dotenv()
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

# Setup Chrome with webdriver-manager (auto installs correct driver)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 1. Go to Speedtest.net
driver.get("https://www.speedtest.net/")
time.sleep(3)

# Click GO button
go_button = driver.find_element(By.CLASS_NAME, "start-text")
go_button.click()

# Wait for results
print("Running speed test, please wait...")
time.sleep(45)  # ⏳ enough time for speed test to finish

# Extract results
download_speed = driver.find_element(By.CLASS_NAME, "download-speed").text
upload_speed = driver.find_element(By.CLASS_NAME, "upload-speed").text
print(f"Download: {download_speed} Mbps, Upload: {upload_speed} Mbps")

# 2. Login to Twitter
driver.get("https://twitter.com/login")
wait = WebDriverWait(driver, 30)

# Enter email
email_input = wait.until(EC.presence_of_element_located((By.NAME, "text")))
email_input.send_keys(TWITTER_EMAIL)
email_input.send_keys(Keys.RETURN)
time.sleep(2)

# Enter password
password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_input.send_keys(TWITTER_PASSWORD)
password_input.send_keys(Keys.RETURN)
time.sleep(5)

# 3. Compose and Post Tweet
tweet_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[aria-label='Tweet text']")))
tweet_message = f"Hey Internet Provider, why is my internet {download_speed}down/{upload_speed}up when I pay for much more? 😡 #SpeedTest"
tweet_box.send_keys(tweet_message)

tweet_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Tweet']")))
tweet_button.click()

print("Tweet sent successfully ✅")
time.sleep(5)

# Close browser
driver.quit()
