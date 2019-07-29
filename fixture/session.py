class SessionHelper:

    def __init__(self,app):
        self.app=app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//input[@name='user']").clear()
        wd.find_element_by_xpath("//input[@name='user']").send_keys(username)
        wd.find_element_by_xpath("//input[@name='pass']").clear()
        wd.find_element_by_xpath("//input[@name='pass']").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username,password)

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, '#')]").click()
        wd.find_element_by_name("user")

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@id='top']/form/b").text == "("+ username + ")"