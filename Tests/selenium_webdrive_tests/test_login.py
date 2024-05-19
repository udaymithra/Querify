# tests/selenium_webdriver_tests/test_login.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.close()

def test_login(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")

    # Wait for the email input field to be present
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "exampleInputEmail1"))
    )
    email_input.send_keys("udaymithra222@gmail.com")
    time.sleep(2)

    # Wait for the password input field to be present
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "exampleInputPassword1"))
    )
    password_input.send_keys("Dhoni@07")
    time.sleep(2)

    # Wait for the login button to be clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/form/button"))
    )
    login_button.click()
    time.sleep(3)

    # Wait for the logout button to be clickable
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "logoutButton"))
    )
    logout_button.click()
