""" file name also start with test_
class name also start with Test

Agenda: must need these
setup Allure on windows
how to Generate Allure Reports
Decorators
How to Share Allure Report

"""

import time
import allure_commons.types
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    # pass method
    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        Create_Button = "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]"

        status = self.driver.find_element(By.XPATH, Create_Button).is_displayed()
        if status:
            allure.attach(self.driver.get_screenshot_as_png(), name="buttonSS", attachment_type=AttachmentType.PNG)
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="button2SS", attachment_type=AttachmentType.PNG)
            assert False
        self.driver.quit()

    # skipped method
    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("skipping test>> Later I will implement")

    # failed mehod
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(25)
        self.driver.maximize_window()
        time.sleep(2)

        self.driver.find_element(By.XPATH,
                                 "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys(
            "Admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys(
            "admin123")
        time.sleep(1)
        self.driver.find_element(By.XPATH,
                                 "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()
        time.sleep(5)
        self.driver.quit()        # now verify the deshboard page shown or not
        actual_title = self.driver.title

        if actual_title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            # attach screenshot into the report formula:(takeSS,name,file format)
            allure.attach(self.driver.get_screenshot_as_png(), name="test_LoginSS", attachment_type=AttachmentType.PNG)
            self.driver.quit()
            assert False


"""  to run pytest we need to run only through terminal: pytest -v -s allureReportDemo\test_orangehrm.py """
""" to make allure, run : pytest -v -s --alluredir="path\reports" allureReportDemo\test_orangehrm.py """
