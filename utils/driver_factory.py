# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# class DriverFactory:
#
#     @staticmethod
#     def get_driver(browser="chrome", headless=False):
#
#         if browser == "chrome":
#             options = Options()
#
#             if headless:
#                 options.add_argument("--headless")
#                 options.add_argument("--window-size=1920,1080")
#             options.add_argument("--no-sandbox")
#             options.add_argument("--disable-dev-shm-usage")
#
#             driver = webdriver.Chrome(options=options)
#             driver.maximize_window()
#             return driver
#
#         else:
#             raise Exception(f"Browser '{browser}' not supported yet")
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome", headless=True):

        if browser.lower() == "chrome":
            options = Options()

            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--disable-gpu")
                options.add_argument("--window-size=1920,1080")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")

            driver = webdriver.Chrome(options=options)
            driver.set_window_size(1920, 1080)   # 👈 VERY IMPORTANT
            return driver

        else:
            raise Exception(f"Browser '{browser}' not supported yet")