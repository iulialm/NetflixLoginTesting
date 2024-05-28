from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class FavoriteListPage(BasePage):
    movie_banner = (By.CSS_SELECTOR, 'a[aria-label="Om vs. albină"]')
    add_button = (By.CSS_SELECTOR, 'button[data-uia="add-to-my-list"]')
    close_button = (By.CSS_SELECTOR, 'span[data-uia="previewModal-closebtn"]')
    my_list_tab = (By.CSS_SELECTOR, 'a[href="/browse/my-list"]')
    my_list_item = (By.CSS_SELECTOR, '//a[@aria-label="Om vs. albină"]')

    def __init__(self, browser):
        self.browser = browser.chrome
        self.wait = WebDriverWait(self.browser,10)

    def click_movie_banner(self):
        self.wait.until(EC.element_to_be_clickable(self.movie_banner)).click()

    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.add_button)).click()

    def click_close_button(self):
        self.wait.until(EC.element_to_be_clickable(self.close_button)).click()

    def click_my_list_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.my_list_tab)).click()

    def verify_my_list_item(self):
        self.wait.until(EC.visibility_of_element_located(self.my_list_item)).is_displayed()