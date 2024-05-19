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
    # Set up the WebDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()  #To  Ensure the browser is closed after each test

def test_signup(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")

    # Click the signup link
    signup_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/form/a"))
    )
    signup_link.click()

    # Fill in the signup form
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "FirstName"))
    )
    first_name.send_keys("Testing")
    time.sleep(2)

    last_name = driver.find_element(By.ID, "LastName")
    last_name.send_keys("User")
    time.sleep(2)

    email = driver.find_element(By.ID, "exampleInputEmail1")
    email.send_keys("kallaudaymithra@gmail.com")
    time.sleep(2)
    password = driver.find_element(By.ID, "InputPassword1")
    password.send_keys("Testing@123")
    time.sleep(2)
    confirm_password = driver.find_element(By.ID, "InputPassword2")
    confirm_password.send_keys("Testing@123")
    time.sleep(2)
    # Submit the signup form
    signup_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button")
    signup_button.click()
    time.sleep(5)

if __name__ == "__main__":
    pytest.main()
