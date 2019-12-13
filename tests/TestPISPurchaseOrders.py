import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPISPurchaseOrders(unittest.TestCase):

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

        #Click on Purchaseorders tab
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[4]/a")
        elem.click()
        time.sleep(1)

        # Clicks on add purchase order button

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/a/span").click()
        time.sleep(2)

        # fill the purchase order details
        elem = driver.find_element_by_id("id_orderId")
        elem.send_keys("4")
        elem = driver.find_element_by_id("id_productname")
        elem.send_keys("MacBook Pro")
        elem = driver.find_element_by_id("id_numberordered")
        elem.send_keys("20")

        time.sleep(2)

        # xpath, clicks on save button for purchase order

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)

        # xpath, clicks on edit purchase order button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/table/tbody/tr/td[4]/a").click()
        time.sleep(2)

        # Edit purchase order details
        elem = driver.find_element_by_id("id_numberordered")
        elem.clear()
        elem.send_keys("30")
        time.sleep(1)

        # xpath, clicks on update button for save supplier

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
