# am importat modului By pentru a putea identifica elemente in pagina dupa anumite criterii
from selenium.webdriver.common.by import By
#am importat clasa WebdDriverWait pentru a putea astepta conditii specifice in timpul testarii
from selenium.webdriver.support.ui import WebDriverWait
#am importat clasa expected_conditions sub abrevierea EC
#este utila atunci cand vrem sa asteptam prezenta unui element , locator, sau text in pagina testata
from selenium.webdriver.support import expected_conditions as EC

#am importat pagina BasePage din folderul base_page
from pages.base_page import BasePage

#clasa LoginPage mosteneste clasa BasePage
class LoginPage(BasePage):
# am definit url-ul de login in pagina
    URL = "https://www.netflix.com/login"
#am definit locatorii pentru elementele din pagina
    USERNAME_INPUT = (By.NAME, "userLoginId")
    PASSWORD_INPUT = (By.NAME, "password")
    SIGN_IN_BTN = (By.XPATH, "//*[@data-uia='login-submit-button']")
    LOGIN_ERROR_MESSAGE = (By.XPATH, "//*[@data-uia='error-message-container']/div/div")

#am definit prin care se navigheaza catre pagina de login
    def navigate_to_login_page(self):
        self.chrome.get(self.URL)

#am definit metoda prin care se  va introduce username-ul in campul aferent
    def enter_username(self, username):
        username_input = self.chrome.find_element(*self.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

#am definit metoda prin care se  va introduce parola in campul aferent
    def enter_password(self, password):
        password_input = self.chrome.find_element(*self.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

#am definit metoda prin care se identifica si se click-uieste pe butonul de sign in
    def click_sign_in_button(self):
        login_button = self.chrome.find_element(*self.SIGN_IN_BTN)
        login_button.click()

#am definit metoda prin care se observa daca mesajul de eroare primit este identic cu mesajul de eroare asteptat
    def check_login_error_message_equals(self, expected_error_message):
        self.check_error_message_equals(*self.LOGIN_ERROR_MESSAGE, expected_error_message)

#am definit metoda prin care se observa daca mesajul de eroare primit contine mesajul de eroare asteptat
    def check_login_error_message_contains(self, expected_error_message):
        self.check_error_message_contains(*self.LOGIN_ERROR_MESSAGE, expected_error_message)

#am definit metoda prin care se verifica daca dupa login, pagina pe care suntem redirectionati este cea corecta.
    def is_redirected_to_browse_page(self):
        expected_url = 'https://www.netflix.com/browse'
        WebDriverWait(self.chrome, 10).until(EC.url_to_be(expected_url))
        current_url = self.chrome.current_url
        print("Expected URL:", expected_url)
        print("Current URL:", current_url)
        return current_url == expected_url
