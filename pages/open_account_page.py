from selenium.webdriver.support import expected_conditions as EC

def open_account(self):
    self.click(self.OPEN_ACCOUNT_LINK)

    # Wait until Open Account page loads
    self.wait.until(EC.url_contains("openaccount.htm"))

    self.click(self.OPEN_BTN)

    print("Waiting for account number...")

    # Wait until account number is present
    return self.wait.until(
        EC.presence_of_element_located(self.ACCOUNT_ID)
    ).text
