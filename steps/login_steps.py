# prin importul * se importa toate simbolurile dintr-un modul, respectiv behave
# behave este biblioteca utilizata pentru BDD (Behavior Driven Development) pentru a defini si rula teste scrise in limbaj natural
# cu ajutorul lui given, when, and, then
from behave import *

#am definit pasii scenariilor create in 1.login.feature, folosind decoratori

# pasul definit in Background, utilizat in toate 3 scenariile
# am speficicat ca in acest pas sa se navigheze pe pagina de login a Netflix
@given("I am on the Netflix login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()

#am definit credentialele invalide pentru acest pas al testul
@when("I enter invalid username and password and click on login button")
def enter_invalid_credentials(context):
    context.login_page.enter_username("utilizatorinvalid@gmail.com")
    context.login_page.enter_password("parolainvalida")
    context.login_page.click_sign_in_button()

#am definit credentialele necesare acestui pas
@when("I enter valid username and invalid password and click on login button")
def enter_valid_username_invalid_password(context):
    context.login_page.enter_username("iulia.almutairi@gmail.com")
    context.login_page.enter_password("parolainvalida")
    context.login_page.click_sign_in_button()

#am definit credentialele valide pentru acest pas al testul
@when("I enter valid username and password and click on login button")
def enter_valid_username_password(context):
    context.login_page.enter_username("iulia.almutairi@gmail.com")
    context.login_page.enter_password("qweasdzxc")
    context.login_page.click_sign_in_button()

#in acest pas am definit ce fel de mesaj exact ar trebuie sa vada utilizatorul
@then('I should see an error message stating "{error_message}"')
def verify_invalid_username_error_message(context, error_message):
    context.login_page.check_login_error_message_equals(error_message)

# am defenit ce fel de mesaj trebuie sa contina mesajul de eroare pe care utilizatorul ar trebui sa il vada
@then('I should see an error message containing "{error_message}"')
def verify_invalid_username_error_message(context, error_message):
    context.login_page.check_login_error_message_contains(error_message)

# am definit ce inseamna redirected to ... daca utilizatorul este logat cu succes
@then('I should be logged in successfully and redirected to the "Choose your profile" page')
def verify_successful_login(context):
    assert context.login_page.is_redirected_to_browse_page(), 'https://www.netflix.com/browse'
