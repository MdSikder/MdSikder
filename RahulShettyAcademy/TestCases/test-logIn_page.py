import time
import allure_commons.types
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
from StructureComplete.Test.TestUtility.screenShot import SS


from structure3.PageObject.POMTC002 import Main

from structure3.PageObject.Locators import Locator
from RahulShettyAcademy.Base.EnvironmentSetup import EnvironmentSetup
from RahulShettyAcademy.PageObjectModel.PomLogIn import Main
from RahulShettyAcademy.PageObjectModel.PomForgotPassword import ForgotPass


def capture_screenshot(d, path):
    file_name = path + "scrrenshot_" + time.asctime().replace(":", "_") + ".png"
    d.save_screenshot(file_name)


@allure.severity(allure.severity_level.NORMAL)
class Test1(EnvironmentSetup):
    @allure.severity(allure.severity_level.MINOR)
    def test1(self):
        pageUrl = "https://rahulshettyacademy.com/locatorspractice/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        main = Main(driver)

        main.UserNameBar.send_keys('porag')
        time.sleep(2)
        main.PasswordBar.send_keys('123!@')
        time.sleep(2)
        main.SingInButton.click()
        time.sleep(2)

        main.ForgotYourPassword.click()
        self.driver.implicitly_wait(5)
        time.sleep(4)

        forgotPass = ForgotPass(driver)

        forgotPass.NameBar.send_keys('porag')
        time.sleep(2)
        forgotPass.EmailBar.send_keys('test@gmail.com')
        time.sleep(2)
        forgotPass.PhoneNumberBar.send_keys('01257894163')
        time.sleep(3)
        forgotPass.ResetButton.click()
        time.sleep(2)
        # forgotPass.PickPass.get_Text()

        forgotPass.GoToLoginButton.click()
        self.driver.implicitly_wait(5)
        time.sleep(3)

        main.UserNameBar.send_keys("Porag")
        time.sleep(1)

        main.PasswordBar.send_keys("rahulshettyacademy")
        time.sleep(2)

        main.SingInButton.click()
        self.driver.implicitly_wait(5)
        time.sleep(5)
        print("LogIn Successfully")
        capture_screenshot(driver, "./loc/")


