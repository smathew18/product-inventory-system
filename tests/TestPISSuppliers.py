import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPISSuppliers(unittest.TestCase):

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

        time.sleep(1)

        #Click on Suppliers tab
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[3]/a")
        elem.click()
        time.sleep(1)

        # Clicks on add suppliers button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/a/span").click()
        time.sleep(2)

        # fill the supplier details
        elem = driver.find_element_by_id("id_suppliername")
        elem.send_keys("Techno Group")
        elem = driver.find_element_by_id("id_supplieraddress")
        elem.send_keys("6001 Dodge Street")
        elem = driver.find_element_by_id("id_suppliercity")
        elem.send_keys("Omaha")
        elem = driver.find_element_by_id("id_supplierstate")
        elem.send_keys("Nebraska")
        elem = driver.find_element_by_id("id_supplierzipcode")
        elem.send_keys("68132")
        time.sleep(2)

        # xpath, clicks on save button for supplier

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)

        # xpath, clicks on edit supplier button

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/table/tbody/tr[1]/td[6]/a").click()
        time.sleep(2)

        # Edit supplier details
        elem = driver.find_element_by_id("id_supplieraddress")
        elem.clear()
        elem.send_keys("8807 Q Street")
        elem = driver.find_element_by_id("id_supplierzipcode")
        elem.clear()
        elem.send_keys("68127")
        time.sleep(1)

        # xpath, clicks on update button for save supplier

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)

        # xpath, clicks on delete supplier button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/table/tbody/tr[3]/td[7]/a").click()
        time.sleep(2)

        driver.switch_to.alert.accept()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
