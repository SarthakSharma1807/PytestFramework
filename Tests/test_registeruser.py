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
