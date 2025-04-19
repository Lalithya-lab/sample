from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

# Correct way to locate chromedriver
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CHROMEDRIVER_PATH = os.path.join(ROOT_DIR, 'chromedriver.exe')

# Set up the service with chromedriver path
chrome_service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)

# Open the Flask app
driver.get("http://localhost:5000")

def test_form_elements():
    assert driver.find_element(By.ID, "name")
    assert driver.find_element(By.ID, "email")
    assert driver.find_element(By.ID, "password")
    assert driver.find_element(By.TAG_NAME, "button")
    print("✅ All form fields are present.")

def test_form_submission():
    driver.find_element(By.ID, "name").send_keys("Alice")
    driver.find_element(By.ID, "email").send_keys("alice@example.com")
    driver.find_element(By.ID, "password").send_keys("securepass123")
    driver.find_element(By.TAG_NAME, "button").click()
    print("✅ Form submission triggered.")

try:
    test_form_elements()
    test_form_submission()
    time.sleep(2)
finally:
    driver.quit()
