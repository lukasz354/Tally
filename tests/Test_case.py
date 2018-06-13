import unittest
from selenium import webdriver


class TestCase(unittest.TestCase):

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        # 1 - Allow all images
        # 2 - Block all images
        # 3 - Block 3rd party images
        profile.set_preference("permissions.default.image", 2)
        self.driver = webdriver.Firefox(firefox_profile=profile)
        profile.set_preference("intl.accept_languages", "pl")
        options = webdriver.FirefoxOptions()
        options.add_argument("--lang=pl")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()



