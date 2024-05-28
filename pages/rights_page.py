from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RightsPage(BasePage):
    manage_profiles_button = (By.CSS_SELECTOR, 'a[data-uia="profile-choices-manage-button"]')
    utilizator_profile_icon = (By.XPATH, '//span[text()="Utilizator Testare"]')
    edit_rights_button = (By.CSS_SELECTOR, 'a[data-uia="profile-edit-button"]')
    enter_password_input = (By.CSS_SELECTOR, 'input[data-uia="input-account-content-restrictions"]')
    continue_rights_process_button = (By.CSS_SELECTOR, 'button[data-uia="btn-account-pin-submit"]')
    check_box_kids_profile = (By.CSS_SELECTOR, 'label[data-uia="label+profile-experience"]')
    save_rights_change = (By.CSS_SELECTOR, 'button[data-uia="btn-account-pin-submit"]')
    back_to_main_screen_button = (By.CSS_SELECTOR, 'button[data-uia="account+side-nav+backButton"]')
    rights_change_check = (By.XPATH, '//li[@class="profile"]//span[text()="Utilizator Testare"]/following-sibling::div[@class="profile-children"]')

    def __init__(self, browser):
        self.browser = browser.chrome
        self.wait = WebDriverWait(self.browser, 10)

    def click_manage_profiles(self):
        self.browser.find_element(*self.manage_profiles_button).click()

    def click_utilizator_profile_icon(self):
        self.browser.find_element(*self.utilizator_profile_icon).click()

    def click_edit_rights_button(self):
        self.browser.find_element(*self.edit_rights_button).click()

    def enter_password(self, password):
        password_field = self.browser.find_element(*self.enter_password_input)
        password_field.send_keys(password)

    def click_continue_rights_process_button(self):
        self.browser.find_element(*self.continue_rights_process_button).click()

    def activate_kids_profile(self):
        self.browser.find_element(*self.check_box_kids_profile).click()

    def click_save_rights_change(self):
        self.browser.find_element(*self.save_rights_change).click()

    def click_back_to_main_screen(self):
        try:
            # Wait for the overlay to disappear
            self.wait.until(EC.invisibility_of_element_located((By.ID, "onetrust-group-container")))
            # Wait for the back button to be clickable
            back_button = self.wait.until(EC.element_to_be_clickable(self.back_to_main_screen_button))
            back_button.click()
        except Exception as e:
            print(f"Error clicking back to main screen button: {e}")

    def check_rights_change(self):
        return self.browser.find_element(*self.rights_change_check).is_displayed()
