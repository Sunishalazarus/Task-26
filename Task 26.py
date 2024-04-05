from Data import data1
from Locators import locator1

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbFill:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Explicit wait
        self.wait = WebDriverWait(self.driver, 30)
        self.act = ActionChains(self.driver)

    def boot(self):
        """
        This method is to open up the chrome browser with the URL and makes the browser to go fullscreen.
        """
        self.driver.get(data1.WebData1().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def quit(self):
        """
        This method is used to close the webbrowser
        """
        self.driver.quit()

    def names(self):
        """
        To fill data and do a search.
        """
        try:
            self.boot()

            for _ in range(9):
                self.act.send_keys(Keys.DOWN).perform()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator1.WebLocators1().expandLocator))).click()
            for _ in range(9):
                self.act.send_keys(Keys.DOWN).perform()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator1.WebLocators1().nameLocator))).send_keys(data1.WebData1().name)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator1.WebLocators1().birthdateLocator))).send_keys(data1.WebData1().birthdate)
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator1.WebLocators1().birthdayLocator))).send_keys(data1.WebData1().birthday)
            for _ in range(9):
                self.act.send_keys(Keys.DOWN).perform()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator1.WebLocators1().awardsLocator))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator1.WebLocators1().birthplaceLocator))).click()
            self.wait.until(EC.visibility_of_element_located((By.XPATH, locator1.WebLocators1().name_birthplaceLocator))).send_keys(data1.WebData1().name_birthplace)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, locator1.WebLocators1().see_resultLocator))).click()
            print("Success: Filled successfully!")

        except Exception as e:
            print("Error", e)
        finally:
            self.quit()

obj = IMDbFill()
obj.names()

"""
Output- Success: Filled successfully!
"""




