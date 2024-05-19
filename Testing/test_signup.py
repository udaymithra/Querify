from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Set up the WebDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the website
        driver.get("http://127.0.0.1:5000")
        time.sleep(1)  # Wait for 1 second

        # Click the signup link
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/a").click()
        time.sleep(2)  # Wait for 2 second

        # Fill in the signup form
        driver.find_element(By.ID, "FirstName").send_keys("Testing")
        time.sleep(2)  # Wait for 2 second

        driver.find_element(By.ID, "LastName").send_keys("User")
        time.sleep(2)  # Wait for 2 second

        driver.find_element(By.ID, "exampleInputEmail1").send_keys("kallaudaymithra@gmail.com")
        time.sleep(2)  # Wait for 2 second

        driver.find_element(By.ID, "InputPassword1").send_keys("Testing@123")
        time.sleep(2)  # Wait for 2 second

        driver.find_element(By.ID, "InputPassword2").send_keys("Testing@123")
        time.sleep(2)  # Wait for 2 second

        # Submit the signup form
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
        time.sleep(2)  # Wait for 2 seconds to observe the result

    finally:
        # Close the browser
        driver.close()

if __name__ == "__main__":
    main()
