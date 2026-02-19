from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OpenAccountPage(BasePage):

    OPEN_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")
    OPEN_BTN = (By.XPATH, "//input[@value='Open New Account']")
    ACCOUNT_ID = (By.ID, "newAccountId")
    def open_account(self):
        self.click(self.OPEN_ACCOUNT_LINK)
    
        # Wait until Open Account page loads
        self.wait.until(EC.url_contains("openaccount.htm"))
    
        self.click(self.OPEN_BTN)
    
        print("Waiting for account number...")
    
        # Wait until account number is visible (STRONG WAIT)
        account_number = self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_ID)
        ).text
    
        print("New account created:", account_number)
    
        return account_number
