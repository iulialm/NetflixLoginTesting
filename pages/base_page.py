#am importat clasaWebDriverWait din modului selenium.webdriver.support.wait
#WebDriverWait este o clasa cu ajutorului careia vom avea timpi de asteptare pana cand elementele din pagina vor fi vizibile
from selenium.webdriver.support.wait import WebDriverWait

#am importat clasa expected_conditions sub abrevierea EC
#este utila atunci cand vrem sa asteptam prezenta unui element , locator, sau text in pagina testata
from selenium.webdriver.support import expected_conditions as EC
#din fisierul browser.py se importa clasa Browser
from browser import Browser


#clasa BasePage mosteste clasa Browser
class BasePage(Browser):

#am definit metoda care va verifica daca textul mesajului de eroare primit este identic cu cel asteptat
    def check_error_message_equals(self, by, selector, expected_error_message):
#timpi de asteptare pana cand elementul devine disponibil in pagina
        error_message_web_element = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located((by, selector)))
#se extrage mesajul primit
        actual_error_message_text = error_message_web_element.text
#se verifica daca mesajul asteptat este identic cu mesajul primit
        assert expected_error_message == actual_error_message_text, f"Error, the message is incorrect. Expected: {expected_error_message}, actual: {actual_error_message_text}"

#am definit metoda care va verifica daca textul mesajului de eroare primit contine fragmente dintr-un mesaj asteptat
    def check_error_message_contains(self, by, selector, expected_error_message):
        error_message_web_element = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located((by, selector)))
        actual_error_message_text = error_message_web_element.text
#se verifica daca mesajul asteptat este integrat in mesajul primit
        assert expected_error_message in actual_error_message_text, f"Error, the actual message does not contain expected. Expected: {expected_error_message}, actual: {actual_error_message_text}"