import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.landingpage import landing_page
from utils.baseclass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self):
        # wait scenario
        time.sleep(2)

        print("registration screen logic")
        lp = landing_page(self.driver)
        lp.search_data_textBox().send_keys("ber")

        time.sleep(2)
        # results = self.driver.find_elements(By.XPATH, "//div[@class='products']/div")
        count = len(lp.add_button_list())
        print(count)
        assert count > 0

        for result in lp.add_button_list():
            result.find_element(By.XPATH, "div/button").click()

        # cart button code
        lp.cart_button_met().click()

        # proceed checkout button
        lp.proceed_button_met().click()

        time.sleep(5)

        # promo code textbox
        lp.promo_textbox_met().send_keys("rahulshettyacademy")

        # Apply button
        lp.apply_button_met().click()


