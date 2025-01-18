from selenium.webdriver.common.by import By


class Homepage:

    signup_login_button = (By.XPATH, "//i[@class='fa fa-lock']")
    logged_in_user = (By.XPATH, "//li/a/b")
    delete_account = (By.LINK_TEXT," Delete Account")
    home_page_logo = (By.XPATH,"//div[@class='logo pull-left']")

    def __init__(self, driver):
        self.driver = driver

    def signuploginbutton(self):
        return self.driver.find_element(*Homepage.signup_login_button)

    def loggedinuser(self):
        return self.driver.find_element(*Homepage.logged_in_user)

    def deleteaccount(self):
        return self.driver.find_element(*Homepage.delete_account)

    def verifyhomepagelogo(self):
        return self.driver.find_element(*Homepage.home_page_logo)
