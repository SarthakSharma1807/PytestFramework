import pytest

from PageObjects.HomePage import Homepage
from PageObjects.SignuploginPage import Signuploginpage
from Utils.Base import Base
from TestData.Testdatadriver import TestDataDriver


class Test_LoginUser(Base):
    def test_loginuser(self,getData):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        signuploginpage = Signuploginpage(self.driver)
        self.verifypresenceoflocator(homepage.home_page_logo)
        log.info("Clicking the Signup/Login button")
        homepage.signuploginbutton().click()
        log.info("Enter name and email address")
        signuploginpage.signupname().send_keys(getData["Name"])
        signuploginpage.signupemail().send_keys(getData["Email"])
        log.info("Click 'Signup' button")
        signuploginpage.signupbutton().click()
        log.info("Verify that 'ENTER ACCOUNT INFORMATION' is visible")
        self.verifypresenceoflocator(signuploginpage.enter_acct_info_text)
        log.info("Fill details: Title, Name, Email, Password, Date of birth")
        signuploginpage.acctinfotitlecheckbox().click()
        signuploginpage.acctinfopwd().send_keys(getData["Pwd"])
        signuploginpage.acctinfodaydropdown(str(getData["Date"]))
        signuploginpage.acctinfomonthdropdown(getData["Month"])
        signuploginpage.acctinfoyeardropdown(str(getData["Year"]))
        log.info("Select checkbox 'Sign up for our newsletter!'")
        signuploginpage.checkboxnewsletter().click()
        log.info("Select checkbox 'Receive special offers from our partners!")
        signuploginpage.checkboxoffers().click()
        log.info(
            "Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number")
        signuploginpage.addressinfofirstname().send_keys(getData["FirstName"])
        signuploginpage.addressinfolastname().send_keys(getData["LastName"])
        signuploginpage.addressinfocompany().send_keys(getData["Company"])
        signuploginpage.address1().send_keys(getData["address1"])
        signuploginpage.address2().send_keys(getData["address2"])
        signuploginpage.addresscountrydropdowm(getData["Country"])
        signuploginpage.addressstate().send_keys(getData["State"])
        signuploginpage.addresscity().send_keys(getData["City"])
        signuploginpage.addresszipcode().send_keys(getData["ZipCode"])
        signuploginpage.addressmobile().send_keys(getData["Mobile"])
        log.info("Click 'Create Account button'")
        signuploginpage.acctcreatebtn().click()
        log.info("Verify that 'ACCOUNT CREATED!' is visible")
        self.verifypresenceoflocator(signuploginpage.acct_created_text)
        log.info("Click 'Continue' button")
        signuploginpage.continuebtn().click()
        log.info("Clicking the logout button")
        homepage.acctlogout().click()
        log.info("Logging in with valid credentials")
        signuploginpage.loginemail().send_keys(getData["Email"])
        signuploginpage.loginpwd().send_keys(getData["Pwd"])
        signuploginpage.loginbtn().click()
        log.info("Verify that 'Logged in as username' is visible")
        self.verifypresenceoflocator(homepage.logged_in_user)
        log.info("Deleting the account")
        homepage.deleteaccount().click()
        signuploginpage.continuebtn().click()


    @pytest.fixture(params=TestDataDriver.getTestData("test_loginuser"))
    def getData(self, request):
        return request.param