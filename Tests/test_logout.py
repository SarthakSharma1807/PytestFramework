import pytest

from PageObjects.HomePage import Homepage
from PageObjects.SignuploginPage import Signuploginpage
from TestData.Testdatadriver import TestDataDriver
from Utils.Base import Base


class Test_Logout(Base):
    def test_logout(self, getData):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        signuploginpage = Signuploginpage(self.driver)
        self.verifypresenceoflocator(homepage.home_page_logo)
        log.info("Clicking the Signup/Login button")
        homepage.signuploginbutton().click()
        log.info("Logging in with valid credentials")
        signuploginpage.loginemail().send_keys(getData["Email"])
        signuploginpage.loginpwd().send_keys(getData["Pwd"])
        log.info("Click the login button")
        signuploginpage.loginbtn().click()
        log.info("Verify that 'Logged in as username' is visible")
        self.verifypresenceoflocator(homepage.logged_in_user)
        log.info("Clicking the logout button")
        homepage.acctlogout().click()
        self.verifypresenceoflocator(homepage.home_page_logo)

    @pytest.fixture(params=TestDataDriver.getTestData("test_logout"))
    def getData(self, request):
        return request.param