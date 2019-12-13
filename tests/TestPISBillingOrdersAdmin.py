import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPISBillingOrdersAdmin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_pis(self):
        user = "instructor"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://pis-assignment4.herokuapp.com/admin/login/?next=/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        driver.get("https://pis-assignment4.herokuapp.com/admin/pis/")
        time.sleep(1)


        #Click on BillingOrders tab
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/table/tbody/tr[1]/th/a")
        elem.click()
        time.sleep(1)

        # Clicks on add billing order button

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
        time.sleep(2)

        # fill the billing order details
        elem = driver.find_element_by_id("id_orderId")
        elem.send_keys("4")
        elem = driver.find_element_by_id("id_billno")
        elem.send_keys("12")
        elem = driver.find_element_by_id("id_billstatus")
        elem.send_keys("Generated")
        time.sleep(2)

        # xpath, clicks on save button for billing order

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(5)

        # xpath, clicks on billing status to edit

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr/th/a").click()
        time.sleep(2)

        # Edit supplier details
        elem = driver.find_element_by_id("id_billstatus")
        elem.clear()
        elem.send_keys("Received")
        time.sleep(1)

        # xpath, clicks on save button for updating billing order

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
