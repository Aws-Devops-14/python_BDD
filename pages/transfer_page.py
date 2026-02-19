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

        # Wait until amount field visible
        self.wait.until(EC.visibility_of_element_located(self.AMOUNT))

        # Enter amount
        self.send_keys(self.AMOUNT, amount)

        # Select From Account
        from_dropdown = Select(self.wait.until(
            EC.presence_of_element_located(self.FROM_ACCOUNT)
        ))
        from_dropdown.select_by_index(0)

        # Select To Account
        to_dropdown = Select(self.wait.until(
            EC.presence_of_element_located(self.TO_ACCOUNT)
        ))
        to_dropdown.select_by_index(1)

        # Click transfer
        self.click(self.TRANSFER_BTN)

        # Wait for success
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TEXT))

        return self.get_text(self.SUCCESS_TEXT)
