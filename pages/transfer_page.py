from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class TransferPage(BasePage):

    TRANSFER_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT = (By.ID, "amount")
    FROM_ACCOUNT = (By.ID, "fromAccountId")
    TO_ACCOUNT = (By.ID, "toAccountId")
    TRANSFER_BTN = (By.XPATH, "//input[@value='Transfer']")
    SUCCESS_TEXT = (By.XPATH, "//h1[contains(text(),'Transfer Complete')]")

    def transfer_funds(self, amount):
    
        self.click(self.TRANSFER_LINK)
    
        self.wait.until(EC.visibility_of_element_located(self.AMOUNT))
    
        self.send_keys(self.AMOUNT, amount)
    
        # Wait until dropdowns are populated
        self.wait.until(lambda driver:
            len(Select(driver.find_element(*self.FROM_ACCOUNT)).options) > 0
        )
    
        self.wait.until(lambda driver:
            len(Select(driver.find_element(*self.TO_ACCOUNT)).options) > 0
        )
    
        from_dropdown = Select(self.driver.find_element(*self.FROM_ACCOUNT))
        to_dropdown = Select(self.driver.find_element(*self.TO_ACCOUNT))
    
        from_accounts = [opt.get_attribute("value") for opt in from_dropdown.options]
        to_accounts = [opt.get_attribute("value") for opt in to_dropdown.options]
    
        print("From accounts:", from_accounts)
        print("To accounts:", to_accounts)
    
        from_dropdown.select_by_value(from_accounts[0])
        to_dropdown.select_by_value(to_accounts[-1])
    
        self.click(self.TRANSFER_BTN)
    
        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TEXT)
        )
    
        return self.get_text(self.SUCCESS_TEXT)
