import time
from behave import when, then
from pages.rights_page import RightsPage
from steps.rename_steps import click_manage_profiles_button, scroll_down  # Import the existing steps

@when('I click on "Utilizator Testare" profile icon')
def click_utilizator_profile_icon(context):
    context.rights_page = RightsPage(context.browser)
    context.rights_page.click_utilizator_profile_icon()
    time.sleep(3)

@when('I press on "Editare" button')
def click_edit_rights_button(context):
    context.rights_page.click_edit_rights_button()
    time.sleep(3)

@when('I enter the password "qweasdzxc"')
def enter_password(context):
    context.rights_page.enter_password("qweasdzxc")
    time.sleep(1)

@when('I press "Continuare" button')
def click_continue_rights_process_button(context):
    context.rights_page.click_continue_rights_process_button()
    time.sleep(3)

@when('I activate "Profil pentru copii"')
def activate_kids_profile(context):
    context.rights_page.activate_kids_profile()
    time.sleep(1)

@when('I press "Salvare"')
def click_save_rights_change(context):
    context.rights_page.click_save_rights_change()
    time.sleep(3)

@when('I click "Inapoi la Netflix"')
def click_back_to_main_screen(context):
    context.rights_page.click_back_to_main_screen()
    time.sleep(3)

@then('"Utilizator Testare" should be a kids profile')
def rights_change_check(context):
    assert context.rights_page.check_rights_change(), "The profile is not marked as a kids profile"
