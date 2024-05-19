import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    # Set up the WebDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.close()  # Close the browser after the test

def test_search_functionality(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")

    # Log in
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("udaymithra222@gmail.com")
    time.sleep(2)  # Wait for 2 second

    driver.find_element(By.ID, "exampleInputPassword1").send_keys("Dhoni@07")
    time.sleep(2)  # Wait for 2 second

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
    time.sleep(2)  # Wait for 2 seconds

    # Search functionality
    driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/form/input").send_keys("Realme")
    time.sleep(3)  # Wait for 3 seconds

    driver.find_element(By.XPATH, "/html/body/header/nav/div[2]/form/button").click()
    time.sleep(3)  # Wait for 3 seconds to observe the result
