import pytest

from PageObjects.HomePage import Homepage
from PageObjects.SignuploginPage import Signuploginpage
from TestData.Testdatadriver import TestDataDriver
from Utils.Base import Base


class Test_incorrectLogin(Base):
    def test_incorrectlogin(self, getData):
        log = self.getlogger()
        homepage = Homepage(self.driver)
        signuploginpage = Signuploginpage(self.driver)
        self.verifypresenceoflocator(homepage.home_page_logo)
        log.info("Clicking the Signup/Login button")
        homepage.signuploginbutton().click()
        log.info("Logging in with invalid credentials")
        signuploginpage.loginemail().send_keys(getData["Email"])
        signuploginpage.loginpwd().send_keys(getData["Pwd"])
        log.info("Click the login button")
        signuploginpage.loginbtn().click()
        log.info("Checking for the incorrect login details message")
        self.verifypresenceoflocator(signuploginpage.login_error)

    @pytest.fixture(params=TestDataDriver.getTestData("test_incorrectlogin"))
    def getData(self, request):
        return request.param
