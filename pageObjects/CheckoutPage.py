from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)
