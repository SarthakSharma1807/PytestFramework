from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Signuploginpage:
    signup_name = (By.XPATH, "//input[@type = 'text']")
    signup_email = (By.XPATH,"//input[@data-qa = 'signup-email']")
    signup_button = (By.XPATH,"//button[@data-qa='signup-button']")

    enter_acct_info_text = (By.XPATH, "//h2[@class='title text-center']/b[text()='Enter Account Information']")
    acct_info_name = (By.XPATH, "//input[@data-qa='name']")
    acct_info_email = (By.XPATH, "//input[@data-qa='email']")
    acct_info_pwd = (By.XPATH, "//input[@data-qa='password']")
    acct_info_day = (By.XPATH, "//select[@data-qa='days']")
    acct_info_month = (By.XPATH, "//select[@data-qa='months']")
    acct_info_year = (By.XPATH, "//select[@data-qa='years']")
    checkbox_newsletter = (By.XPATH, "//input[@name='newsletter']")
    checkbox_offers =  (By.XPATH, "//input[@name='optin']")
    address_info_first_name = (By.XPATH,"//input[@data-qa='first_name']")
    address_info_last_name = (By.XPATH,"//input[@data-qa='last_name']")
    address_info_company = (By.XPATH,"//input[@data-qa='company']")
    address_address1 = (By.XPATH,"//input[@data-qa='address']")
    address_address2 = (By.XPATH, "//input[@data-qa='address2']")
    address_country = (By.XPATH, "//input[@data-qa='country']")
    address_state = (By.XPATH, "//input[@data-qa='state']")
    address_city = (By.XPATH, "//input[@data-qa='city']")
    address_zipcode = (By.XPATH, "//input[@data-qa='zipcode']")
    address_mobile = (By.XPATH, "//input[@data-qa='mobile_number']")
    acct_create_btn = (By.XPATH, "//input[@data-qa='create_account']")

    acct_created_text = (By.XPATH, "//h2[@data-qa='account-created']")
    continue_btn = (By.LINK_TEXT, "Continue")
    acct_deleted_text = (By.XPATH, "//h2[@data-qa='account-deleted']")

    def __init__(self, driver):
        self.driver = driver

    def signupname(self):
        return self.driver.find_element(*Signuploginpage.signup_name)

    def signupemail(self):
        return self.driver.find_element(*Signuploginpage.signup_email)

    def signupbutton(self):
        return self.driver.find_element(*Signuploginpage.signup_button)

    def enteracctinfotext(self):
        return self.driver.find_element(*Signuploginpage.enter_acct_info_text)

    def acctinfoname(self):
        return self.driver.find_element(*Signuploginpage.acct_info_name)

    def acctinfoemail(self):
        return self.driver.find_element(*Signuploginpage.acct_info_email)

    def acctinfopwd(self):
        return self.driver.find_element(*Signuploginpage.acct_info_pwd)

    def acctinfodaydropdown(self, Selection):
        day = Select(self.driver.find_element(*Signuploginpage.acct_info_day))
        day.select_by_visible_text(Selection)

    def acctinfomonthdropdown(self, Selection):
        day = Select(self.driver.find_element(*Signuploginpage.acct_info_month))
        day.select_by_visible_text(Selection)

    def acctinfoyeardropdown(self, Selection):
        day = Select(self.driver.find_element(*Signuploginpage.acct_info_year))
        day.select_by_visible_text(Selection)

    def checkboxnewsletter(self):
        return self.driver.find_element(*Signuploginpage.checkbox_newsletter)

    def checkboxoffers(self):
        return self.driver.find_element(*Signuploginpage.checkbox_offers)

    def addressinfofirstname(self):
        return self.driver.find_element(*Signuploginpage.address_info_first_name)

    def addressinfolastname(self):
        return self.driver.find_element(*Signuploginpage.address_info_last_name)

    def addressinfocompany(self):
        return self.driver.find_element(*Signuploginpage.address_info_company)

    def address1(self):
        return self.driver.find_element(*Signuploginpage.address_address1)

    def address2(self):
        return self.driver.find_element(*Signuploginpage.address_address2)

    def addresscountrydropdowm(self, Selection):
        country = Select(self.driver.find_element(*Signuploginpage.address_country))
        country.select_by_visible_text(Selection)

    def addressstate(self):
        return self.driver.find_element(*Signuploginpage.address_state)

    def addresscity(self):
        return self.driver.find_element(*Signuploginpage.address_city)

    def addresszipcode(self):
        return self.driver.find_element(*Signuploginpage.address_zipcode)

    def address_mobile(self):
        return self.driver.find_element(*Signuploginpage.address_mobile)

    def acctcreatebtn(self):
        return self.driver.find_element(*Signuploginpage.acct_create_btn)


