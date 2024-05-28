import time
from behave import when, then
from pages.rename_page import RenamePage

@when('I click on "Gestionarea profilurilor" button')
def click_manage_profiles_button(context):
    context.rename_page = RenamePage(context.browser.chrome)
    context.rename_page.click_manage_profiles_button()
    time.sleep(5)  # Pause for 5 seconds to see the action

@when('I click on "abc" profile icon')
def click_abc_profile_icon(context):
    try:
        context.rename_page.click_abc_profile_icon()
        print("Clicked on abc Profile icon")
    except Exception as e:
        print(f"Error clicking on abc Profile icon: {e}")
    time.sleep(5)  # Pause for 5 seconds to see the action

@when('I rename the user profile to "{new_name}"')
def rename_user_profile(context, new_name):
    context.rename_page.rename_profile(new_name)
    time.sleep(5)  # Pause for 5 seconds to see the action

@when('I scroll down')
def scroll_down(context):
    context.browser.chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Pause for 5 seconds to see the action

@when('I click on "Salvare" button')
def click_save_button(context):
    context.rename_page.click_save_button()
    time.sleep(5)  # Pause for 5 seconds to see the action

@when('I click on "Gata" button')
def click_done_button(context):
    context.rename_page.click_done_button()
    time.sleep(5)  # Pause for 5 seconds to see the action

@then('I should see a profile named "Utilizator Testare" on the browse page')
def verify_profile_renamed(context):
    profile_renamed = context.rename_page.is_profile_renamed("Utilizator Testare")
    print(f"Profile renamed: {profile_renamed}")  # Debug statement
    assert profile_renamed, "Profile was not renamed to Utilizator Testare"
