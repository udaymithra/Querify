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

def test_edit_profile(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")

    # Log in
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("udaymithra222@gmail.com")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "exampleInputPassword1").send_keys("Dhoni@07")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
    time.sleep(2)  # Wait for 2 seconds

    # Edit profile
    driver.find_element(By.XPATH, "//*[@id='userName']").click()
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div[1]/img").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div[1]/input").clear()
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div[1]/input").send_keys("Udaymithra")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div[2]/img").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div[2]/input").clear()
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/form/div[2]/input").send_keys("K")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.XPATH, "//*[@id='saveProfile']").click()
    time.sleep(3)  # Wait for 3 seconds to observe the result

if __name__ == "__main__":
    pytest.main()
