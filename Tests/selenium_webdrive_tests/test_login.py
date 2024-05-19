from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Set up the WebDriver using WebDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the website
        driver.get("http://127.0.0.1:5000")

        # Wait for the email input field to be present
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "exampleInputEmail1"))
        )
        email_input.send_keys("udaymithra222@gmail.com")
        time.sleep(1)

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


    finally:
        # Close the browser
        driver.close()

if __name__ == "__main__":
    main()
