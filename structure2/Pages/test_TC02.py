import time

from selenium.webdriver import Keys

from structure2.base.Base import EnvironmentSetup
from structure2.POM.POMTest1 import Locator

from selenium.webdriver.common.by import By

Loc = Locator()


class Home2(EnvironmentSetup):

    def test1(self):
        pageUrl = "https://www.facebook.com/"
        driver = self.driver
        self.driver.get(pageUrl)
        self.driver.implicitly_wait(20)
        time.sleep(2)

        driver.find_element(By.XPATH, Loc.text2).send_keys('porag', Keys.ENTER)
        time.sleep(10)
