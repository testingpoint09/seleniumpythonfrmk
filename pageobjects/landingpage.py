from selenium.webdriver.common.by import By


class landing_page:

    def __init__(self, driver):
        self.driver = driver

    # searchbox xpath
    searchBox = (By.XPATH, "//input[@type='search']")

    # buttons list xpath
    results = (By.XPATH, "//div[@class='products']/div")

    #cart xpath
    cart_button=(By.CSS_SELECTOR, "img[alt='Cart']")

    #add_to_cart xpath
    add_to_cart_button=(By.XPATH, "div/button")

    #proceed xpath
    proceed_button=(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    #promo code textbox xpath
    promo_code_txt=(By.CSS_SELECTOR, ".promoCode")

    #apply button xpath
    apply_button=(By.CSS_SELECTOR, ".promoBtn")

    #promo message
    promo_message=(By.CLASS_NAME, "promoInfo")



    def search_data_textBox(self):
        return self.driver.find_element(*landing_page.searchBox)

    def add_button_list(self):
        return self.driver.find_elements(*landing_page.results)



    def cart_button_met(self):
        return self.driver.find_element(*landing_page.cart_button)

    def proceed_button_met(self):
        return self.driver.find_element(*landing_page.proceed_button)

    def promo_textbox_met(self):
        return self.driver.find_element(*landing_page.promo_code_txt)

    def apply_button_met(self):
        return self.driver.find_element(*landing_page.apply_button)

    def promo_message_met(self):
        return self.driver.find_element(*landing_page.promo_message)