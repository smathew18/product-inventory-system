import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestPISProductAdmin(unittest.TestCase):

    def setUp(self) :
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
        #Click on Product tab

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/table/tbody/tr[2]/th/a")
        elem.click()
        time.sleep(1)

        # Clicks on add product button
        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/ul/li/a").click()
        time.sleep(2)

        # fill the product details
        elem = driver.find_element_by_id("id_user")
        elem.send_keys("instructor")
        elem = driver.find_element_by_id("id_productname")
        elem.send_keys("Microsoft Surface")
        elem = driver.find_element_by_id("id_producttype")
        elem.send_keys("Laptop")
        elem = driver.find_element_by_id("id_price")
        elem.send_keys("1200")
        elem = driver.find_element_by_id("id_status")
        elem.send_keys("Item ready to be purchased")
        elem = driver.find_element_by_id("id_comments")
        elem.send_keys("No Issues")
        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys("20")
        time.sleep(2)

        # xpath, clicks on save button for add product

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(2)

        # xpath, clicks on product to edit

        elem = driver.find_element_by_xpath("/html/body/div/div[3]/div/div/form/div[2]/table/tbody/tr[1]/th/a").click()
        time.sleep(2)

        # Edit product details
        elem = driver.find_element_by_id("id_user")
        elem.send_keys("instructor")
        elem = driver.find_element_by_id("id_productname")
        elem.clear()
        elem.send_keys("Google Pixel2")
        elem = driver.find_element_by_id("id_producttype")
        elem.clear()
        elem.send_keys("Mobile Device")
        time.sleep(1)

        # xpath, clicks on save button for edit product

        elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
