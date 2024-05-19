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

        # Log in
        driver.find_element(By.ID, "exampleInputEmail1").send_keys("udaymithra222@gmail.com")
        time.sleep(2)  # Wait for 2 second

        driver.find_element(By.ID, "exampleInputPassword1").send_keys("Dhoni@07")
        time.sleep(2)  # Wait for 2 second

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/button").click()
        time.sleep(2)  # Wait for 2 seconds

        # Click on profile
        driver.find_element(By.XPATH, "//*[@id='userName']").click()
        time.sleep(2)  # Wait for 2 seconds

        driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[3]/button/img").click()
        time.sleep(3)  # Wait for 3 seconds to observe the result


        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/form/button[2]").click() 
        time.sleep(3)

    finally:
        # Close the browser
        driver.close()

if __name__ == "__main__":
    main()
