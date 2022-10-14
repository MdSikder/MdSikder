from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By


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
            assert True
        else:
            assert False
        self.driver.quit()
