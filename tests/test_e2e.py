import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self, setup):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkOutPage = CheckoutPage(self.driver)
        products = checkOutPage.getCardTitles()

        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
                product.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[contains(@class, 'checkbox-primary')]").click()
        self.driver.find_element_by_css_selector("input[value='Purchase']").click()
        successMessage = self.driver.find_element_by_css_selector("div[class*='alert-dismissible']").text
        assert "Success!" in successMessage
        self.driver.get_screenshot_as_file("screen.png")
