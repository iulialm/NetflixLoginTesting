from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ManagePage(BasePage):
    add_profile_icon = (By.CSS_SELECTOR, 'a[data-uia="profile-choices-create-button"]')
    profile_name_input = (By.CSS_SELECTOR, 'input[data-uia="profile-create-name-input"]')
    save_button = (By.CSS_SELECTOR, 'span[data-uia="profile-create-continue-button"]')
    profile_name_elements = (By.CSS_SELECTOR, 'span.profile-name')

    def __init__(self, browser):
        self.browser = browser

    def click_add_profile_icon(self):
        add_profile_button = self.browser.find_element(*self.add_profile_icon)
        add_profile_button.click()
        print("Add Profile icon clicked")  # Debug statement

    def enter_profile_name(self, profile_name):
        profile_name_input = self.browser.find_element(*self.profile_name_input)
        profile_name_input.clear()
        profile_name_input.send_keys(profile_name)
        print(f"Profile name entered: {profile_name}")  # Debug statement

    def click_save_button(self):
        save_button = self.browser.find_element(*self.save_button)
        save_button.click()
        print("Save button clicked")  # Debug statement

    def is_profile_created(self, profile_name):
        profiles = self.browser.find_elements(*self.profile_name_elements)
        print(f"Profiles found: {[profile.text for profile in profiles]}")  # Debug statement
        return any(profile.text == profile_name for profile in profiles)