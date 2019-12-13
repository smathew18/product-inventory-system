import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPISLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_pis(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://pis-assignment4.herokuapp.com/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://pis-assignment4.herokuapp.com/home/")
        assert "Logged In"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
