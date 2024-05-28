from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class RenamePage(BasePage):
    manage_profiles_button = (By.CSS_SELECTOR, 'a[data-uia="profile-choices-manage-button"]')
    abc_profile_icon = (By.XPATH, '//span[text()="abc"]')
    profile_name_input = (By.CSS_SELECTOR, 'input[data-uia="profile-edit-name-input"]')
    save_button = (By.CSS_SELECTOR, 'button[data-uia="profile-save-button"]')
    done_button = (By.CSS_SELECTOR, 'a.profile-button.preferred-action[href="/ProfilesGate"]')
    profile_name_elements = (By.CSS_SELECTOR, 'span.profile-name')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)  # Add a wait

    def click_manage_profiles_button(self):
        button = self.wait.until(EC.presence_of_element_located(self.manage_profiles_button))
        print(f"Found Manage Profiles button: {button}")
        button.click()
        print("Clicked on Manage Profiles button")

    def click_abc_profile_icon(self):
        profile_icon = self.wait.until(EC.presence_of_element_located(self.abc_profile_icon))
        print(f"Found abc Profile icon: {profile_icon}")
        profile_icon.click()
        print("Clicked on abc Profile icon")

    def rename_profile(self, new_name):
        profile_name_input = self.wait.until(EC.presence_of_element_located(self.profile_name_input))
        print(f"Found Profile Name input: {profile_name_input}")
        profile_name_input.clear()
        profile_name_input.send_keys(new_name)
        print(f"Renamed profile to: {new_name}")

    def click_save_button(self):
        save_button = self.wait.until(EC.presence_of_element_located(self.save_button))
        print(f"Found Save button: {save_button}")
        save_button.click()
        print("Clicked on Save button")

    def click_done_button(self):
        done_button = self.wait.until(EC.presence_of_element_located(self.done_button))
        print(f"Found Done button: {done_button}")
        done_button.click()
        print("Clicked on Done button")

    def is_profile_renamed(self, profile_name):
        profiles = self.wait.until(EC.presence_of_all_elements_located(self.profile_name_elements))
        print(f"Found profiles: {[profile.text for profile in profiles]}")
        return any(profile.text == profile_name for profile in profiles)