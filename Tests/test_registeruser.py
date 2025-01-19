from PageObjects.HomePage import Homepage
from PageObjects.SignuploginPage import Signuploginpage
from Utils.Base import Base


class Test_registeruser(Base):
    def test_registeruser(self):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        signuploginpage = Signuploginpage(self.driver)
        self.verifypresenceoflocator(homepage.home_page_logo)
        log.info("Clicking the Signup/Login button")
        homepage.signuploginbutton().click()
        log.info("Enter name and email address")
        signuploginpage.signupname().send_keys("Steve Rogers")
        signuploginpage.signupemail().send_keys("steve@avengers.com")
        log.info("Click 'Signup' button")
        signuploginpage.signupbutton().click()
        log.info("Verify that 'ENTER ACCOUNT INFORMATION' is visible")
        self.verifypresenceoflocator(signuploginpage.enter_acct_info_text)
        log.info("Fill details: Title, Name, Email, Password, Date of birth")
        signuploginpage.acctinfotitlecheckbox().click()
        signuploginpage.acctinfopwd().send_keys("peggycarter")
        signuploginpage.acctinfodaydropdown("18")
        signuploginpage.acctinfomonthdropdown("July")
        signuploginpage.acctinfoyeardropdown("1994")
        log.info("Select checkbox 'Sign up for our newsletter!'")
        signuploginpage.checkboxnewsletter().click()
        log.info("Select checkbox 'Receive special offers from our partners!")
        signuploginpage.checkboxoffers().click()
        log.info("Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number")
        signuploginpage.addressinfofirstname().send_keys("Steve")
        signuploginpage.addressinfolastname().send_keys("Rogers")
        signuploginpage.addressinfocompany().send_keys("AvengersHQ")
        signuploginpage.address1().send_keys("Brooklyn")
        signuploginpage.address2().send_keys("New York")
        signuploginpage.addresscountrydropdowm("United States")
        signuploginpage.addressstate().send_keys("New York")
        signuploginpage.addresscity().send_keys("New York")
        signuploginpage.addresszipcode().send_keys("1234567")
        signuploginpage.addressmobile().send_keys("1234567890")
        log.info("Click 'Create Account button'")
        signuploginpage.acctcreatebtn().click()
        log.info("Verify that 'ACCOUNT CREATED!' is visible")
        self.verifypresenceoflocator(signuploginpage.acct_created_text)
        log.info("Click 'Continue' button")
        signuploginpage.continuebtn().click()
        log.info("Verify that 'Logged in as username' is visible")
        self.verifypresenceoflocator(homepage.logged_in_user)
        log.info("Click 'Delete Account' button")
        homepage.deleteaccount().click()
        log.info("Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button")
        self.verifypresenceoflocator(signuploginpage.acct_deleted_text)
        signuploginpage.continuebtn().click()

