import unittest

from selenium.webdriver.chrome import webdriver


class Browser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

