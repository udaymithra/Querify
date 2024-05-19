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

def test_create_post(driver):
    # Open the website
    driver.get("http://127.0.0.1:5000")

    # Log in
    driver.find_element(By.ID, "exampleInputEmail1").send_keys("udaymithra222@gmail.com")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "exampleInputPassword1").send_keys("Dhoni@07")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
    time.sleep(2)  # Wait for 2 seconds

    # Create a post
    driver.find_element(By.CLASS_NAME, "postButton").click()
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "title").send_keys("Automation Testing")
    time.sleep(2)  # Wait for 2 seconds

    # Clear and enter content into the editor
    editor = driver.find_element(By.CLASS_NAME, "ql-editor")
    editor.clear()
    time.sleep(2)  # Wait for 2 seconds
    editor.send_keys("How to do Automation Testing and where can I learn it? Any links please")
    time.sleep(2)  # Wait for 2 seconds

    driver.find_element(By.ID, "saveFormButton").click()
    time.sleep(2)  # Wait for 2 seconds
    driver.find_element(By.ID, "submitButton").click()
    time.sleep(3)  # Wait for 3 seconds to observe the result

if __name__ == "__main__":
    pytest.main()
