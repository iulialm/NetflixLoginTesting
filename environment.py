#din fisiwerul browser.py am importat clasa Browser
from browser import Browser

# before_all este o metoda care contine toate instructiunile care trebuie rulate inainte de orice test
# este echivalentul metodei setUp de la libraria unit test
from pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser()  # instantiem un obiect din clasa Browser
    context.login_page = LoginPage()  # am instantiat un obiect din clasa Login_page
    context.browser.maximise_window()


# after_all este o metoda care contine toate instructiunile care trebuie rulate inainte de orice test
# este echivalentul metodei tearDown de la libraria unit test
def after_all(context):
    context.browser.close_browser()  # apelam metoda close_browser pe baza obiectului instantiat din clasa Browser()