import time

from behave import given, when, then
from pages.manage_page import ManagePage

@given('I am logged in to Netflix')
def logged_in_Netflix(context):
    expected_url = 'https://www.netflix.com/browse'
    current_url = context.browser.chrome.current_url
    print(f"Current URL: {current_url}")  # Debug statement
    assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

@when('I click on the "Adauga un profil" icon')
def click_add_profile_icon(context):
    context.manage_page = ManagePage(context.browser.chrome)
    context.manage_page.click_add_profile_icon()
    print("Clicked on Add Profile icon")  # Debug statement
    time.sleep(5)

@when('I enter "{profile_name}" into the profile name input field')
def enter_profile_name(context, profile_name):
    context.manage_page.enter_profile_name(profile_name)
    print(f"Entered profile name: {profile_name}")  # Debug statement
    time.sleep(5)

@when('I click the "Continuare" button')
def click_save_button(context):
    context.manage_page.click_save_button()
    print("Clicked on Save button")  # Debug statement
    time.sleep(5)

@then('a profile named "{profile_name}" should be created')
def verify_profile_created(context, profile_name):
    profile_created = context.manage_page.is_profile_created(profile_name)
    print(f"Profile created: {profile_created}")  # Debug statement
    assert profile_created, f"Profile named {profile_name} was not created"
    time.sleep(5)