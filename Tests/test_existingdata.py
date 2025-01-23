import pytest

from PageObjects.HomePage import Homepage
from PageObjects.SignuploginPage import Signuploginpage
from TestData.Testdatadriver import TestDataDriver
from Utils.Base import Base


class Test_existingData(Base):
    def test_existingdata(self, getData):
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
        log.info("Verifying error message for data already exists")
        self.verifypresenceoflocator(signuploginpage.sign_email_already_exist)

    @pytest.fixture(params=TestDataDriver.getTestData("test_existingdata"))
    def getData(self, request):
        return request.param