from selenium.webdriver.common.by import By


class Homepage:

    signup_login_button = (By.LINK_TEXT, " Signup / Login")
    logged_in_user = (By.XPATH, "//li/a/b")
    delete_account = (By.LINK_TEXT," Delete Account")

    def __init__(self, driver):
        self.driver = driver

    def signuploginbutton(self):
        return self.driver.find_element(*Homepage.signup_login_button)

    def loggedinuser(self):
        return self.driver.find_element(*Homepage.logged_in_user)

    def deleteaccount(self):
        return self.driver.find_element(*Homepage.delete_account)