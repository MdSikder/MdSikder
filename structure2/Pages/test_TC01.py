import time

from selenium.webdriver import Keys

from structure2.base.Base import EnvironmentSetup
from structure2.POM.POMTest1 import Locator

from selenium.webdriver.common.by import By
from structure2.screenShot.screenShot import SS

Loc = Locator()
ss_path = "/files/"


class Home(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://www.google.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)
        ss = SS(driver)

        driver.find_element(By.XPATH, Loc.text).send_keys('kabir', Keys.ENTER)
        time.sleep(10)
        ss.ScreenShot(ss_path + "home1.png")
