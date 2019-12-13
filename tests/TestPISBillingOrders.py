import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPISBillingOrders(unittest.TestCase):

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


        #Click on BillingOrders tab
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[5]/a")
        elem.click()
        time.sleep(1)

        # Clicks on create billing order button

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/a/span").click()
        time.sleep(2)

        # fill the billing order details
        elem = driver.find_element_by_id("id_orderId")
        elem.send_keys("2")
        elem = driver.find_element_by_id("id_billno")
        elem.send_keys("120")
        elem = driver.find_element_by_id("id_billstatus")
        elem.send_keys("Generated")
        time.sleep(2)

        # xpath, clicks on save button for billing order

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)

        # xpath, clicks on edit billing order button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/table/tbody/tr/td[4]/a").click()
        time.sleep(2)

        # Edit supplier details
        elem = driver.find_element_by_id("id_billstatus")
        elem.clear()
        elem.send_keys("Received")
        time.sleep(1)

        # xpath, clicks on update button for billing orderr

        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
