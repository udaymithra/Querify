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
    driver.quit()  # Ensure the browser is closed after each test

def test_login_error(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")

    # Enter email
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("udaymithra222@gmail.com")
    time.sleep(2)  # Wait for 2 seconds

    # Enter incorrect password
    driver.find_element(By.ID, "exampleInputPassword1").send_keys("Welcome@1")
    time.sleep(2)  # Wait for 2 seconds

    # Click the login button
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
    time.sleep(5)  # Wait for 5 seconds to allow error messages to appear

if __name__ == "__main__":
    pytest.main()
