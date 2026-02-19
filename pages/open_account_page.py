from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class OpenAccountPage(BasePage):

    OPEN_ACCOUNT_LINK = (By.LINK_TEXT, "Open New Account")
    OPEN_BTN = (By.XPATH, "//input[@value='Open New Account']")
    ACCOUNT_ID = (By.ID, "newAccountId")
    def open_account(self):
        self.click(self.OPEN_ACCOUNT_LINK)
    
        # Wait for page URL
        self.wait.until(EC.url_contains("openaccount.htm"))
    
        # STRONG WAIT for button to be clickable
        open_btn = self.wait.until(
            EC.element_to_be_clickable(self.OPEN_BTN)
        )
        open_btn.click()
    
        print("Waiting for account number...")
    
        # STRONG WAIT for account number to be visible
        account_number = self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_ID)
        ).text
    
        print("New account created:", account_number)
    
        return account_number
