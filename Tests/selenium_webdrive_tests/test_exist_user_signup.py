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

def test_exist_user_signup(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")
    time.sleep(1)  # Wait for 1 second

    # Navigate to the signup page
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/a").click()
    time.sleep(2)  # Wait for 2 seconds

    # Fill in the signup form
    driver.find_element(By.ID, "FirstName").send_keys("Udaymithra")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "LastName").send_keys("Kalla")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "exampleInputEmail1").send_keys("udaymithra222@gmail.com")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "InputPassword1").send_keys("Dhoni@07")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "InputPassword2").send_keys("Dhoni@07")
    time.sleep(2)  # Wait for 2 seconds

    # Submit the form
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
    time.sleep(5)  # Wait for 5 seconds to ensure the form is submitted
