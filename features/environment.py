from utils.driver_factory import DriverFactory

def before_all(context):
    context.driver = DriverFactory.get_driver(browser="chrome", headless=True)

def after_all(context):
    context.driver.quit()
