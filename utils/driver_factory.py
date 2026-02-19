from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome"):

        if browser == "chrome":
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            driver = webdriver.Chrome(options=options)
            driver.maximize_window()
            return driver

        else:
            raise Exception(f"Browser '{browser}' not supported yet")
