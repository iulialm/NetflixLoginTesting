import time
from behave import when, then
from pages.search_page import Searchbar

@when('I enter in "Utilizator Testare" profile')
def step_enter_profile(context):
    context.search_page = Searchbar(context.browser)
    context.search_page.click_profile_icon()
    time.sleep(3)  # Wait for the page to load

@when('I click on search icon')
def step_click_search_icon(context):
    context.search_page.click_search_icon()

@when('I type "{query}"')
def step_type_search_query(context, query):
    context.search_page.type_search_query(query)
    time.sleep(2)  # Wait for search results to load

@then('An error message contains "{message}" should be displayed on the screen')
def step_verify_error_message(context, message):
    assert context.search_page.verify_error_message(message), f"Error message '{message}' not found"

@then('I should be able to see the result on the screen')
def step_verify_search_result(context):
    assert context.search_page.verify_search_result(), "Search result not found"

@when('I click on search box')
def step_click_search_box(context):
    context.search_page.click_search_icon()

@when('I delete the written content')
def step_delete_written_content(context):
    context.search_page.clear_search_box()
    time.sleep(1)  # Wait for the search box to clear