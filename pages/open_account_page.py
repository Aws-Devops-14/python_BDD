from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OpenAccountPage(BasePage):

    OPEN_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")
    OPEN_BTN = (By.XPATH, "//input[@value='Open New Account']")
    ACCOUNT_ID = (By.ID, "newAccountId")

    def open_account(self):
        self.click(self.OPEN_ACCOUNT_LINK)
        self.click(self.OPEN_BTN)
        print("Waiting for account number...")
        return self.get_text(self.ACCOUNT_ID)
