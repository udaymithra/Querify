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

def test_comment_to_post(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")

    # Log in
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("udaymithra222@gmail.com")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "exampleInputPassword1").send_keys("Dhoni@07")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
    time.sleep(2)  # Wait for 2 seconds

    # Navigate to the post
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/a").click()
    time.sleep(2)  # Wait for 2 seconds

    # Add a comment
    driver.find_element(By.XPATH, "//*[@id='editor']/div[1]").send_keys("Testing comment with Selenium")
    driver.find_element(By.ID, "saveCommentButton").click()
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "addCommentButton").click()
    time.sleep(3)  # Wait for 3 seconds

if __name__ == "__main__":
    pytest.main()
