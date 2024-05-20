#am importat din selenium modului webdriver pentru a putea permite interactiunea cu un browser web
from selenium import webdriver


class Browser:
# am creat clasa Browser si am initializat Chrome
    chrome = webdriver.Chrome()

#metoda ajuta ca fereasta sa se maximizeze
    def maximise_window(self):
        self.chrome.maximize_window()

#metoda ajuta ca fereastra sa se inchida
    def close_browser(self):
        self.chrome.quit()
