from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper

class Application:
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unknown browser: %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.wd.implicitly_wait(3)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
