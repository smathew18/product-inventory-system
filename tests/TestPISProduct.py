import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPISProduct(unittest.TestCase):

    def setUp(self) :
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
        #Click on Product tab
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[2]/a")
        elem.click()
        time.sleep(1)

        # Clicks on add product button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/a/span").click()
        time.sleep(2)

        # fill the product details
        elem = driver.find_element_by_id("id_productname")
        elem.send_keys("MacBook Pro")
        elem = driver.find_element_by_id("id_producttype")
        elem.send_keys("Laptop")
        elem = driver.find_element_by_id("id_price")
        elem.send_keys("1000")
        elem = driver.find_element_by_id("id_status")
        elem.send_keys("Item ready to be purchased")
        elem = driver.find_element_by_id("id_comments")
        elem.send_keys("No Issues")
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("20")
        time.sleep(2)

        # xpath, clicks on save button for add product
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)

        # xpath, clicks on edit product button

        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/table/tbody/tr[1]/td[7]/a").click()
        time.sleep(2)

        # Edit product details
        elem = driver.find_element_by_id("id_productname")
        elem.clear()
        elem.send_keys("Samsung Galaxy")
        elem = driver.find_element_by_id("id_producttype")
        elem.clear()
        elem.send_keys("Mobile Device")
        time.sleep(1)

        # xpath, clicks on update button for edit product
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)

        # xpath, clicks on delete product button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/table/tbody/tr[2]/td[8]/a").click()
        time.sleep(2)

        driver.switch_to.alert.accept()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
