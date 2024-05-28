import time
from behave import given, when, then
from pages.favorite_list_page import FavoriteListPage

@given('I am on result search page')
def step_on_search_page(context):
    context.browser.chrome.get("https://www.netflix.com/Kids/search?q=Om%20vs.%20albin%C4%83")
    context.favorite_list_page = FavoriteListPage(context.browser)

@when('I click on the movie banner')
def step_click_movie_banner(context):
    context.favorite_list_page.click_movie_banner()
    time.sleep(3)

@when('I click "+" button')
def step_click_add_button(context):
    context.favorite_list_page.click_add_button()
    time.sleep(3)

@when('I click "X" button')
def step_click_close_button(context):
    context.favorite_list_page.click_close_button()
    time.sleep(3)
@when('I click on " Lista mea" tab')
def step_click_my_list_tab(context):
    context.favorite_list_page.click_my_list_tab()
    time.sleep(3)

@then('I should see "Om vs. albină" in my list')
def step_verify_movie_in_my_list(context):
    assert context.favorite_list_page.verify_movie_in_my_list(), "Movie not found in my list"