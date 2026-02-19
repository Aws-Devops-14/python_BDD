from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class TransferPage(BasePage):

    TRANSFER_LINK = (By.LINK_TEXT, "Transfer Funds")
    AMOUNT = (By.ID, "amount")
    TRANSFER_BTN = (By.XPATH, "//input[@value='Transfer']")
    SUCCESS_TEXT = (By.XPATH, "//h1[contains(text(),'Transfer Complete')]")

    def transfer_funds(self, amount):
        # Click transfer funds link
        self.click(self.TRANSFER_LINK)

        # Wait until amount field is visible
        self.wait.until(EC.visibility_of_element_located(self.AMOUNT))

        # Enter amount
        self.send_keys(self.AMOUNT, amount)

        # Click transfer button
        self.click(self.TRANSFER_BTN)

        # Wait until success message appears
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TEXT))

        return self.get_text(self.SUCCESS_TEXT)

