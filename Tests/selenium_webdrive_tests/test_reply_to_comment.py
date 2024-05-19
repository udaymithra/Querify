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

def test_reply_to_comment(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")

    # Log in
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("kallaudaymithra@gmail.com")
    time.sleep(2)  # Wait for 2 second

    driver.find_element(By.ID, "exampleInputPassword1").send_keys("Testing@123")
    time.sleep(2)  # Wait for 2 second

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
    time.sleep(2)  # Wait for 2 seconds

    # Click the View Comments button
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/a").click()
    time.sleep(2)  # Wait for 2 second

    # Click the reply button under a comment 
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[3]/span[1]/a").click() 
    time.sleep(2)

    # Type a reply message under the comment
    driver.find_element(By.XPATH, '//*[@id="replyEditor"]/div[1]/p').send_keys("Testing Reply to Comment")
    time.sleep(3)

    driver.find_element(By.ID, "replyCommentButton").click()
    time.sleep(2)  # Wait for 2 second
