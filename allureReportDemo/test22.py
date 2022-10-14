import time

from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By


class TestHRM:
    # pass method

    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[2]/div[1]/div[2]/input[1]").send_keys("admin123")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()
        time.sleep(5)
        self.driver.quit()
