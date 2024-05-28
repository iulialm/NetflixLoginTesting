from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class Searchbar(BasePage):
    profile_icon = (By.XPATH, '//span[text()="Utilizator Testare"]')
    search_icon = (By.CSS_SELECTOR, 'button[data-uia="search-box-launcher"]')
    search_input = (By.CSS_SELECTOR, 'input[data-uia="search-box-input"]')
    delete_action = (By.CSS_SELECTOR, 'input[data-uia="search-box-input"]')
    error_message = (By.XPATH, '//p[contains(text(), "Căutarea pentru „Film inexistent” nu a returnat rezultate.")]')
    search_result = (By.XPATH, '//a[@aria-label="Om vs. albină"]')

    def __init__(self, browser):
        self.browser = browser.chrome
        self.wait = WebDriverWait(self.browser, 10)

    def click_profile_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.profile_icon)).click()

    def click_search_icon(self):
        self.wait.until(EC.element_to_be_clickable(self.search_icon)).click()

    def type_search_query(self, query):
        search_input_element = self.wait.until(EC.element_to_be_clickable(self.search_input))
        search_input_element.clear()
        search_input_element.send_keys(query)

    def clear_search_box(self):
        search_input_element = self.wait.until(EC.element_to_be_clickable(self.delete_action))
        search_input_element.clear()

    def verify_search_result(self):
        return self.wait.until(EC.visibility_of_element_located(self.search_result)).is_displayed()

    def verify_error_message(self, message):
        error_element = self.wait.until(EC.visibility_of_element_located(self.error_message))
        return message in error_element.text