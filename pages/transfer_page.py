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

        # Wait until dropdowns have options
        from_element = self.wait.until(
            EC.presence_of_element_located(self.FROM_ACCOUNT)
        )
        to_element = self.wait.until(
            EC.presence_of_element_located(self.TO_ACCOUNT)
        )

        from_dropdown = Select(from_element)
        to_dropdown = Select(to_element)

        # Ensure options exist
        if len(from_dropdown.options) > 0:
            from_dropdown.select_by_index(0)

        if len(to_dropdown.options) > 1:
            to_dropdown.select_by_index(1)
        else:
            to_dropdown.select_by_index(0)

        self.click(self.TRANSFER_BTN)

        self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_TEXT)
        )

        return self.get_text(self.SUCCESS_TEXT)
